import os, re, requests
from pathlib import Path
from datetime import date

PUBMED='https://eutils.ncbi.nlm.nih.gov/entrez/eutils'
OPENALEX='https://api.openalex.org/works'

def _title(s): return re.sub(r'[^a-z0-9]+',' ',(s or '').lower()).strip()

def search(topic, years=5, limit=20):
    start=date.today().year-years; rows=[]
    p=requests.get(f'{PUBMED}/esearch.fcgi',params={'db':'pubmed','term':f'({topic}) AND ({start}:3000[pdat])','retmode':'json','retmax':limit,'sort':'relevance'},timeout=40); p.raise_for_status()
    ids=p.json().get('esearchresult',{}).get('idlist',[])
    if ids:
        s=requests.get(f'{PUBMED}/esummary.fcgi',params={'db':'pubmed','id':','.join(ids),'retmode':'json'},timeout=40); s.raise_for_status(); data=s.json().get('result',{})
        for pid in ids:
            x=data.get(pid,{})
            rows.append({'title':x.get('title',''),'year':str(x.get('pubdate',''))[:4],'authors':', '.join(a.get('name','') for a in x.get('authors',[])[:8]),'doi':'','pmid':pid,'source':'PubMed','url':f'https://pubmed.ncbi.nlm.nih.gov/{pid}/','pdf_url':''})
    p=requests.get(OPENALEX,params={'search':topic,'filter':f'from_publication_date:{start}-01-01,is_paratext:false','per-page':limit,'mailto':os.getenv('OPENALEX_EMAIL','')},timeout=40); p.raise_for_status()
    for x in p.json().get('results',[]):
        doi=(x.get('doi') or '').replace('https://doi.org/',''); loc=x.get('best_oa_location') or x.get('primary_location') or {}; pdf=loc.get('pdf_url','') if loc else ''
        rows.append({'title':x.get('display_name',''),'year':str(x.get('publication_year','')),'authors':', '.join((a.get('author') or {}).get('display_name','') for a in x.get('authorships',[])[:8]),'doi':doi,'pmid':'','source':'OpenAlex','url':x.get('doi') or x.get('id',''),'pdf_url':pdf})
    seen=set(); out=[]
    for r in rows:
        k=(r['doi'] or _title(r['title'])).lower()
        if k and k not in seen: seen.add(k); out.append(r)
    return out

def download_pdfs(rows, folder):
    Path(folder).mkdir(parents=True,exist_ok=True); downloaded=[]
    for i,r in enumerate(rows,1):
        url=r.get('pdf_url','')
        if not url: continue
        try:
            resp=requests.get(url,timeout=60,headers={'User-Agent':'DailyPaperWriter/1.0'}); resp.raise_for_status()
            if 'pdf' not in resp.headers.get('content-type','').lower() and not resp.content.startswith(b'%PDF'): continue
            safe=re.sub(r'[^A-Za-z0-9._-]+','_',r['title'])[:90].strip('_') or f'paper_{i}'
            path=Path(folder)/f'{i:03d}_{safe}.pdf'; path.write_bytes(resp.content); r['local_pdf']=str(path); downloaded.append(r)
        except Exception as e: r['pdf_error']=str(e)
    return downloaded
