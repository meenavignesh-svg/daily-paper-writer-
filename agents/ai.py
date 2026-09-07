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
        'researcher': (
            'You are a careful human bioinformatics researcher. '
            'Organize the supplied bibliographic records into a clear, relevance-ranked evidence overview. '
            'Write in plain, natural academic English. Never invent findings. '
            'Flag which records need full-text verification.'
        ),
        'analyst': (
            'You are a careful human scientific analyst. '
            'Compare the supplied bibliographic evidence. '
            'Identify themes, methodological differences, likely gaps and conflicts in natural academic prose. '
            'Do not invent results. Mark unsupported statements [VERIFY]. '
            'Avoid robotic or formulaic AI phrasing.'
        ),
        'writer': (
            'You are a careful human bioinformatics researcher writing a literature review. '
            'Write in natural, fluent academic English that sounds like a real researcher, not an AI. '
            'Use varied sentence length, precise but readable language, and a measured scholarly tone. '
            'Avoid buzzwords, repetitive stock phrases, and overly polished or robotic AI style. '
            'Draft only from the supplied evidence and analysis. Cite records as [1], [2], etc. '
            'Never invent facts, numbers, methods, datasets, or quotations. '
            'When evidence is insufficient write [VERIFY]. '
            'Produce these sections in clear prose: Title, Abstract, Introduction, Evidence Synthesis, '
            'Methods and Datasets Observed, Research Gaps, Limitations, Conclusion, References. '
            'The final text must read as if a thoughtful human wrote it slowly and carefully.'
        )
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

    # Do not send temperature — some models only accept the default
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
