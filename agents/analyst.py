import json, os, requests


def analyze(topic, question, papers):
    base=os.getenv("LLM_BASE_URL","").rstrip("/"); key=os.getenv("LLM_API_KEY",""); model=os.getenv("LLM_MODEL","")
    evidence="\n".join(f"[{i}] {p['title']} | {p.get('year','')} | DOI {p.get('doi') or 'none'} | {p.get('url','')}" for i,p in enumerate(papers,1))
    if not (base and key and model):
        return {"summary":"LLM not configured; manual evidence review required.","agreements":[],"conflicts":[],"gaps":["Extract methods, datasets, results and limitations from the original papers."],"structure":["Introduction","Methods","Evidence synthesis","Limitations and gaps","Conclusion"],"verification":["Verify every claim against the original paper."]}
    prompt=f'''You are AI-2, a rigorous scientific analyst. Topic: {topic}\nQuestion: {question}\nAnalyze ONLY the supplied paper metadata. Do not invent findings or claim to have read full text. Identify likely evidence clusters, agreements/conflicts only when supported by metadata, research gaps that are explicitly safe to flag, a review structure, and verification tasks. Return valid JSON with keys summary, agreements, conflicts, gaps, structure, verification.\n\nPAPERS:\n{evidence}'''
    r=requests.post(f"{base}/chat/completions",headers={"Authorization":f"Bearer {key}","Content-Type":"application/json"},json={"model":model,"messages":[{"role":"user","content":prompt}],"temperature":0.1},timeout=120)
    r.raise_for_status(); text=r.json()["choices"][0]["message"]["content"]
    text=text.strip().removeprefix("```json").removesuffix("```").strip()
    try: return json.loads(text)
    except Exception: return {"summary":text,"agreements":[],"conflicts":[],"gaps":[],"structure":[],"verification":["Review AI output before use."]}
