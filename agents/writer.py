import os, requests


def write_review(topic, question, papers, analysis):
    base=os.getenv("LLM_BASE_URL","").rstrip("/"); key=os.getenv("LLM_API_KEY",""); model=os.getenv("LLM_MODEL","")
    refs="\n".join(f"[{i}] {p['title']} ({p.get('year','')}). {p.get('journal','')}. DOI: {p.get('doi') or 'none'}. URL: {p.get('url','')}" for i,p in enumerate(papers,1))
    if not (base and key and model):
        return f"# Review Paper Draft\n\n## Introduction\nTopic: {topic}\n\nResearch question: {question}\n\n## Evidence base\n{refs}\n\n## Discussion\n[NEEDS VERIFICATION] Configure the LLM and verify the original papers before drafting scientific claims.\n\n## References\n{refs}"
    prompt=f'''You are AI-3, a conservative scientific review writer. Write an accumulating review-paper draft for: {topic}\nResearch question: {question}\nUse ONLY the supplied evidence and AI-2 analysis. Never invent findings, numbers, methods, datasets, citations, or quotations. Do not imply full-text reading unless the evidence supplied says it was read. Every substantive claim must cite one or more supplied reference numbers like [1]. If evidence is insufficient, write [VERIFY]. Produce sections: Title, Abstract, Introduction, Evidence Synthesis, Research Gaps, Limitations, Conclusion, References. This is a draft for human scientific review, not a publication-ready claim of fact.\n\nAI-2 ANALYSIS:\n{analysis}\n\nPAPERS:\n{refs}'''
    r=requests.post(f"{base}/chat/completions",headers={"Authorization":f"Bearer {key}","Content-Type":"application/json"},json={"model":model,"messages":[{"role":"user","content":prompt}],"temperature":0.2},timeout=180)
    r.raise_for_status(); return r.json()["choices"][0]["message"]["content"]
