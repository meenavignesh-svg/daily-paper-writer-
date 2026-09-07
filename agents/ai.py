import os, json, requests

def call(role, topic, question, evidence):
    base=os.getenv('LLM_BASE_URL','').rstrip('/'); key=os.getenv('LLM_API_KEY',''); model=os.getenv('LLM_MODEL','')
    if not (base and key and model): return {'status':'disabled','text':'LLM not configured'}
    prompts={
      'researcher': 'You are AI Researcher. Organize the supplied bibliographic records into a relevance-ranked evidence queue. Never invent findings. Identify which records need full-text verification.',
      'analyst': 'You are AI Scientific Analyst. Compare the supplied bibliographic evidence, identify themes, methodological differences, likely gaps and conflicts. Do not invent results. Mark unsupported statements [VERIFY].',
      'writer': 'You are AI Scientific Writer. Draft a cautious literature-review section from the supplied evidence and analysis. Cite records as [1], [2], etc. Never invent facts. Use [VERIFY] when evidence is insufficient.'}
    content=f"ROLE INSTRUCTION:\n{prompts[role]}\n\nTOPIC: {topic}\nQUESTION: {question}\n\nEVIDENCE:\n{json.dumps(evidence,ensure_ascii=False)[:60000]}"
    r=requests.post(f'{base}/chat/completions',headers={'Authorization':f'Bearer {key}','Content-Type':'application/json'},json={'model':model,'messages':[{'role':'user','content':content}],'temperature':0.2},timeout=180); r.raise_for_status()
    return {'status':'ok','text':r.json()['choices'][0]['message']['content']}
