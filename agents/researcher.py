import os, re, time
from pathlib import Path
import requests

PUBMED = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
OPENALEX = "https://api.openalex.org/works"


def _clean(s):
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def _get(url, **kwargs):
    r = requests.get(url, timeout=45, **kwargs)
    r.raise_for_status()
    return r


def pubmed_search(query, start_year, limit):
    p = {"db":"pubmed","term":f"({query}) AND ({start_year}:3000[pdat])","retmode":"json","retmax":limit,"sort":"relevance"}
    ids = _get(f"{PUBMED}/esearch.fcgi", params=p).json().get("esearchresult",{}).get("idlist",[])
    if not ids: return []
    data = _get(f"{PUBMED}/esummary.fcgi", params={"db":"pubmed","id":",".join(ids),"retmode":"json"}).json().get("result",{})
    out=[]
    for pid in ids:
        x=data.get(pid,{})
        out.append({"source":"PubMed","title":x.get("title", ""),"year":str(x.get("pubdate", ""))[:4],"doi":"","pmid":pid,"journal":x.get("fulljournalname", ""),"authors":", ".join(a.get("name","") for a in x.get("authors",[])[:8]),"url":f"https://pubmed.ncbi.nlm.nih.gov/{pid}/"})
    return out


def openalex_search(query, start_year, limit):
    p={"search":query,"filter":f"from_publication_date:{start_year}-01-01,is_paratext:false","per-page":limit,"mailto":os.getenv("OPENALEX_EMAIL","")}
    out=[]
    for x in _get(OPENALEX, params=p).json().get("results",[]):
        doi=(x.get("doi") or "").replace("https://doi.org/","")
        pl=x.get("primary_location") or {}
        src=pl.get("source") or {}
        oa=x.get("open_access") or {}
        best=x.get("best_oa_location") or {}
        out.append({"source":"OpenAlex","title":x.get("display_name",""),"year":str(x.get("publication_year", "")),"doi":doi,"pmid":"","journal":src.get("display_name",""),"authors":", ".join((a.get("author") or {}).get("display_name","") for a in x.get("authorships",[])[:8]),"url":x.get("doi") or x.get("id",""),"oa_url":best.get("pdf_url") or best.get("landing_page_url") or "","is_oa":bool(oa.get("is_oa"))})
    return out


def collect(query, start_year, limit):
    rows=pubmed_search(query,start_year,limit)+openalex_search(query,start_year,limit)
    seen=set(); out=[]
    for r in rows:
        key=(r.get("doi") or _clean(r.get("title"))).lower()
        if key and key not in seen:
            seen.add(key); out.append(r)
    return out


def download_open_access_pdfs(rows, out_dir):
    out=Path(out_dir); out.mkdir(parents=True,exist_ok=True)
    results=[]
    for i,r in enumerate(rows,1):
        url=r.get("oa_url") or ""
        if not url or not r.get("is_oa"):
            r["pdf_path"]=""; r["pdf_status"]="No confirmed open-access PDF"
            results.append(r); continue
        try:
            resp=requests.get(url,timeout=60,headers={"User-Agent":"DailyPaperWriter/1.0 research-assistant"})
            ctype=resp.headers.get("content-type","").lower()
            if resp.ok and ("pdf" in ctype or resp.content[:4]==b"%PDF"):
                safe=re.sub(r"[^A-Za-z0-9._-]+","_",r.get("title",f"paper_{i}"))[:100]
                path=out/f"{i:03d}_{safe}.pdf"
                path.write_bytes(resp.content)
                r["pdf_path"]=str(path); r["pdf_status"]="Downloaded open-access PDF"
            else: r["pdf_path"]=""; r["pdf_status"]="OA location did not return a PDF"
        except Exception as e:
            r["pdf_path"]=""; r["pdf_status"]=f"PDF download failed: {e}"
        time.sleep(0.2)
        results.append(r)
    return results
