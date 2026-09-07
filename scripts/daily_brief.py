import json
from datetime import date
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
CFG = json.loads((ROOT / "config" / "topics.json").read_text(encoding="utf-8"))
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)


def search_openalex(query, years, limit):
    start = date.today().year - years
    r = requests.get("https://api.openalex.org/works", params={
        "search": query,
        "filter": f"from_publication_date:{start}-01-01,is_paratext:false",
        "per-page": limit,
    }, timeout=30)
    r.raise_for_status()
    return r.json().get("results", [])

rows = search_openalex(CFG["topic"], CFG["years"], CFG["papers"])
lines = [f"# Daily Bioinformatics Research Brief — {date.today()}", "", f"**Topic:** {CFG['topic']}", f"**Question:** {CFG['question']}", "", "## Papers to read", ""]

for i, x in enumerate(rows, 1):
    doi = x.get("doi") or "Not available"
    lines += [
        f"### {i}. {x.get('display_name', 'Untitled')}",
        f"- Year: {x.get('publication_year', '')}",
        f"- DOI: {doi}",
        f"- OpenAlex: {x.get('id', '')}",
        "- Finding: **[READ AND EXTRACT]**",
        "- Methods/dataset: **[READ AND EXTRACT]**",
        "- Limitation: **[READ AND EXTRACT]**",
        "",
    ]

lines += ["## Today's task", "- [ ] Read 2–3 papers", "- [ ] Extract evidence", "- [ ] Record one contradiction or research gap", "- [ ] Update the manuscript only with verified evidence"]
(OUT / f"{date.today()}-brief.md").write_text("\n".join(lines), encoding="utf-8")
print(f"Generated {len(rows)} paper entries")
