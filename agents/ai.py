import os
import json
import requests

def call(role, topic, question, evidence):
    base = os.getenv('LLM_BASE_URL', '').rstrip('/')
    key = os.getenv('LLM_API_KEY', '')
    model = os.getenv('LLM_MODEL', '')

    if not (base and key and model):
        return {
            'status': 'disabled',
            'text': 'LLM not configured. Set LLM_BASE_URL, LLM_API_KEY and LLM_MODEL secrets.'
        }

    prompts = {
        'researcher': 'You are AI Researcher. Organize the supplied bibliographic records into a relevance-ranked evidence table. Never invent findings. Identify which records need full-text verification.',
        'analyst': 'You are AI Scientific Analyst. Compare the supplied bibliographic evidence, identify themes, methodological differences, likely gaps and conflicts. Do not invent results. Mark unsupported statements [VERIFY].',
        'writer': 'You are AI Scientific Writer. Draft a cautious literature-review section from the supplied evidence and analysis. Cite records as [1], [2], etc. Never invent facts. Use [VERIFY] when evidence is insufficient. Produce clear sections: Title, Abstract, Introduction, Evidence Synthesis, Methods and Datasets, Research Gaps, Limitations, Conclusion, References.'
    }

    # Keep evidence short to avoid token / size related errors
    evidence_str = json.dumps(evidence, ensure_ascii=False)
    if len(evidence_str) > 25000:
        evidence_str = evidence_str[:25000] + '... [truncated]'

    content = (
        f"ROLE INSTRUCTION:\n{prompts.get(role, '')}\n\n"
        f"TOPIC: {topic}\nQUESTION: {question}\n\n"
        f"EVIDENCE:\n{evidence_str}"
    )

    # Do not send temperature — some models (e.g. gpt-5.6-luna) only accept the default
    payload = {
        'model': model,
        'messages': [{'role': 'user', 'content': content}]
    }

    try:
        r = requests.post(
            f'{base}/chat/completions',
            headers={
                'Authorization': f'Bearer {key}',
                'Content-Type': 'application/json'
            },
            json=payload,
            timeout=180
        )

        if r.status_code >= 400:
            try:
                err_body = r.json()
            except Exception:
                err_body = r.text[:1500]
            return {
                'status': 'error',
                'text': (
                    f'LLM call failed with HTTP {r.status_code}.\n'
                    f'URL: {base}/chat/completions\n'
                    f'Model: {model}\n'
                    f'Provider response: {err_body}\n\n'
                    f'Fallback: LLM drafting skipped. Use the literature list and downloaded PDFs instead.'
                )
            }

        data = r.json()
        return {'status': 'ok', 'text': data['choices'][0]['message']['content']}

    except Exception as e:
        return {
            'status': 'error',
            'text': (
                f'LLM call failed ({type(e).__name__}): {e}\n\n'
                f'Fallback: LLM drafting skipped. Use the literature list and downloaded PDFs instead.'
            )
        }
