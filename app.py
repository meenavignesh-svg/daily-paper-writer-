import os
import re
import json
from datetime import date
from urllib.parse import quote

import pandas as pd
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Daily Bioinformatics Paper Writer", page_icon="🧬", layout="wide")

PUBMED = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
OPENALEX = "https://api.openalex.org/works"


def clean_title(value):
    return re.sub(r"[^a-z0-9]+", " ", (value or "").lower()).strip()


def pubmed_search(query, start_year, limit):
    term = f'({query}) AND ({start_year}:3000[pdat])'
    params = {"db": "pubmed", "term": term, "retmode": "json", "retmax": limit, "sort": "relevance"}
    r = requests.get(PUBMED, params=params, timeout=30)
    r.raise_for_status()
    ids = r.json().get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []
    summary = requests.get(
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi",
        params={"db": "pubmed", "id": ",".join(ids), "retmode": "json"},
        timeout=30,
    )
    summary.raise_for_status()
    data = summary.json().get("result", {})
    rows = []
    for pid in ids:
        x = data.get(pid, {})
        rows.append({
            "source": "PubMed", "title": x.get("title", ""), "year": str(x.get("pubdate", ""))[:4],
            "doi": "", "pmid": pid, "url": f"https://pubmed.ncbi.nlm.nih.gov/{pid}/",
            "journal": x.get("fulljournalname", ""), "authors": ", ".join(a.get("name", "") for a in x.get("authors", [])[:6])
        })
    return rows


def openalex_search(query, start_year, limit):
    params = {
        "search": query, "filter": f"from_publication_date:{start_year}-01-01,is_paratext:false",
        "per-page": limit, "mailto": os.getenv("OPENALEX_EMAIL", "")
    }
    r = requests.get(OPENALEX, params=params, timeout=30)
    r.raise_for_status()
    rows = []
    for x in r.json().get("results", []):
        doi = x.get("doi") or ""
        rows.append({
            "source": "OpenAlex", "title": x.get("display_name", ""), "year": str(x.get("publication_year", "")),
            "doi": doi.replace("https://doi.org/", ""), "pmid": "", "url": x.get("doi") or x.get("id", ""),
            "journal": (x.get("primary_location") or {}).get("source", {}).get("display_name", "") if x.get("primary_location") else "",
            "authors": ", ".join((a.get("author") or {}).get("display_name", "") for a in x.get("authorships", [])[:6])
        })
    return rows


def merge(rows):
    seen = set()
    out = []
    for row in rows:
        key = row["doi"].lower().strip() if row["doi"] else clean_title(row["title"])
        if not key or key in seen:
            continue
        seen.add(key)
        out.append(row)
    return out


def bibtex(rows):
    blocks = []
    for i, r in enumerate(rows, 1):
        key = f"paper{i}_{re.sub(r'[^a-z0-9]', '', r['title'].lower())[:25]}"
        blocks.append("@article{%s,\n  title={%s},\n  author={%s},\n  year={%s},\n  journal={%s},\n  doi={%s},\n  url={%s}\n}" % (
            key, r["title"], r["authors"], r["year"], r["journal"], r["doi"], r["url"]
        ))
    return "\n\n".join(blocks)


def brief(topic, question, rows):
    lines = [f"# Daily Research Brief — {date.today()}", "", f"**Topic:** {topic}", f"**Research question:** {question}", "", "## Evidence queue", ""]
    for i, r in enumerate(rows, 1):
        lines += [f"### {i}. {r['title']}", f"- Source: {r['source']}", f"- Year: {r['year']}", f"- Authors: {r['authors'] or 'Not supplied'}", f"- DOI: {r['doi'] or 'Not supplied'}", f"- Link: {r['url']}", "- Key finding: **[READ ABSTRACT/FULL TEXT AND VERIFY]**", "- Methods/dataset: **[EXTRACT]**", "- Limitation: **[EXTRACT]**", ""]
    lines += ["## Researcher checklist", "- [ ] Read the original papers", "- [ ] Verify every numerical/result claim", "- [ ] Verify every DOI/reference", "- [ ] Record methods and datasets", "- [ ] Record limitations and contradictions", "- [ ] Add only evidence-supported claims to the manuscript"]
    return "\n".join(lines)


def ai_draft(topic, question, rows):
    base = os.getenv("LLM_BASE_URL", "").rstrip("/")
    key = os.getenv("LLM_API_KEY", "")
    model = os.getenv("LLM_MODEL", "")
    if not base or not key or not model:
        return "LLM is not configured. Add LLM_BASE_URL, LLM_API_KEY and LLM_MODEL to .env."
    evidence = "\n".join(f"[{i}] {r['title']} ({r['year']}) DOI:{r['doi'] or 'none'} URL:{r['url']}" for i, r in enumerate(rows, 1))
    prompt = f"""You are a scientific writing assistant. Draft a cautious literature-review section for this topic: {topic}\nResearch question: {question}\n\nONLY use the supplied evidence list. Do not invent facts, statistics, methods, citations or papers. If evidence is insufficient, write [NEEDS VERIFICATION]. Use citation numbers like [1]. Do not claim to have read full text.\n\nEVIDENCE:\n{evidence}\n"""
    r = requests.post(f"{base}/chat/completions", headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"}, json={"model": model, "messages": [{"role": "user", "content": prompt}], "temperature": 0.2}, timeout=120)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

st.title("🧬 Daily Bioinformatics Paper Writer")
st.caption("Search → organize → verify → write. AI never replaces checking the original paper.")

with st.sidebar:
    st.header("Research settings")
    topic = st.text_input("Topic", "AI and machine learning in protein function prediction")
    question = st.text_area("Research question", "How are machine-learning methods being used to predict protein function, what datasets and evaluation metrics are used, and what limitations remain?")
    years = st.slider("Years back", 1, 15, 5)
    limit = st.slider("Papers per database", 5, 50, 20)
    run = st.button("🔎 Search literature", type="primary", use_container_width=True)

if run:
    start_year = date.today().year - years
    with st.spinner("Searching PubMed and OpenAlex…"):
        try:
            rows = merge(pubmed_search(topic, start_year, limit) + openalex_search(topic, start_year, limit))
            st.session_state["rows"] = rows
            st.session_state["topic"] = topic
            st.session_state["question"] = question
        except Exception as e:
            st.error(f"Search failed: {e}")

rows = st.session_state.get("rows", [])
if rows:
    st.success(f"Found {len(rows)} deduplicated papers.")
    df = pd.DataFrame(rows)
    st.dataframe(df[["source", "title", "year", "doi", "journal", "url"]], use_container_width=True, hide_index=True)

    b1, b2, b3 = st.columns(3)
    b1.download_button("⬇️ Literature CSV", df.to_csv(index=False), "literature.csv", "text/csv", use_container_width=True)
    b2.download_button("📚 BibTeX", bibtex(rows), "references.bib", "text/plain", use_container_width=True)
    b3.download_button("📝 Daily brief", brief(topic, question, rows), f"brief-{date.today()}.md", "text/markdown", use_container_width=True)

    st.divider()
    st.subheader("✍️ Evidence-constrained drafting")
    st.write("The draft prompt is intentionally restricted to the papers retrieved above.")
    if st.button("Generate AI draft"):
        with st.spinner("Drafting…"):
            try:
                st.session_state["draft"] = ai_draft(topic, question, rows)
            except Exception as e:
                st.session_state["draft"] = f"AI request failed: {e}"
    if st.session_state.get("draft"):
        st.markdown(st.session_state["draft"])
        st.download_button("⬇️ Download draft", st.session_state["draft"], f"draft-{date.today()}.md", "text/markdown")
else:
    st.info("Choose a focused question and click Search literature to begin today's research session.")

st.divider()
st.caption("Built for research assistance. Always verify claims, references, methods and results against the original sources before submission.")
