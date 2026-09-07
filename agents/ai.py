import os
import json
import requests

def call(role, topic, question, evidence):
    base = os.getenv('LLM_BASE_URL', '').rstrip('/')
    key = os.getenv('LLM_API_KEY', '')
    model = os.getenv('LLM_MODEL', '')

    if not (base and key and model):
        return {'status': 'disabled', 'text': 'LLM not configured. Set LLM_BASE_URL, LLM_API_KEY and LLM_MODEL secrets.'}

    prompts = {
        'researcher': 'You are AI Researcher. Organize the supplied bibliographic records into a relevance-ranked evidence table. Never invent findings. Identify which records need full-text verification.',
        'analyst': 'You are AI Scientific Analyst. Compare the supplied bibliographic evidence, identify themes, methodological differences, likely gaps and conflicts. Do not invent results. Mark unsupported statements [VERIFY].',
        'writer': 'You are AI Scientific Writer. Draft a cautious literature-review section from the supplied evidence and analysis. Cite records as [1], [2], etc. Never invent facts. Use [VERIFY] when evidence is insufficient.'
    }

    content = (
        f"ROLE INSTRUCTION:\n{prompts.get(role, '')}\n\n"
        f"TOPIC: {topic}\nQUESTION: {question}\n\n"
        f"EVIDENCE:\n{json.dumps(evidence, ensure_ascii=False)[:60000]}"
    )

    try:
        r = requests.post(
            f'{base}/chat/completions',
            headers={
                'Authorization': f'Bearer {key}',
                'Content-Type': 'application/json'
            },
            json={
                'model': model,
                'messages': [{'role': 'user', 'content': content}],
                'temperature': 0.2
            },
            timeout=180
        )
        r.raise_for_status()
        return {'status': 'ok', 'text': r.json()['choices'][0]['message']['content']}
    except Exception as e:
        # Never crash the pipeline because of an LLM problem
        return {
            'status': 'error',
            'text': f'LLM call failed ({type(e).__name__}): {e}\n\nFallback: LLM drafting skipped. Use the literature list and downloaded PDFs instead.'
        }
