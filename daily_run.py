import os
import json
import zipfile
from pathlib import Path
from datetime import date
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from agents.researcher import search, download_pdfs
from agents.ai import call
from agents.emailer import send

def pdf(path, title, text):
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(str(path), pagesize=A4, rightMargin=45, leftMargin=45, topMargin=45, bottomMargin=45)
    story = [Paragraph(title, styles['Title']), Spacer(1, 12)]
    for block in text.split('\n'):
        if block.strip():
            story.append(Paragraph(block.replace('&', '&amp;'), styles['BodyText']))
            story.append(Spacer(1, 7))
    doc.build(story)

def fallback_review(topic, question, rows):
    """Generate a structured, usable review from metadata when LLM is unavailable."""
    day = date.today()
    lines = [
        f'# Daily Literature Review: {topic}',
        f'Date: {day}',
        '',
        '## Research Question',
        question,
        '',
        '## Summary',
        f'This document compiles {len(rows)} recent papers related to the topic. '
        'AI drafting was unavailable, so the content below is built directly from bibliographic metadata. '
        'Each entry includes title, authors, year, source, DOI/URL, and a reminder to extract findings from the original paper. '
        'This is an evidence-collection scaffold, not a finished scientific review.',
        '',
        '## Evidence Table (Bibliographic)',
        ''
    ]

    # Group roughly by year for readability
    by_year = {}
    for r in rows:
        y = r.get('year') or 'Unknown'
        by_year.setdefault(y, []).append(r)

    for year in sorted(by_year.keys(), reverse=True):
        lines.append(f'### {year}')
        lines.append('')
        for i, r in enumerate(by_year[year], 1):
            title = r.get('title') or 'Untitled'
            authors = r.get('authors') or 'Authors not supplied'
            source = r.get('source') or ''
            doi = r.get('doi') or ''
            url = r.get('url') or ''
            pmid = r.get('pmid') or ''

            lines.append(f'**{title}**')
            lines.append(f'- Authors: {authors}')
            lines.append(f'- Source: {source}')
            if doi:
                lines.append(f'- DOI: {doi}')
            if pmid:
                lines.append(f'- PMID: {pmid}')
            if url:
                lines.append(f'- Link: {url}')
            lines.append('- Key finding / methods / datasets / limitations: **Extract from original paper after reading.**')
            lines.append('')

    lines += [
        '## Recommended Next Steps',
        '1. Open the attached individual PDFs (or follow the DOI/URL links).',
        '2. For each relevant paper, extract: main method, datasets used, evaluation metrics, key quantitative results, and stated limitations.',
        '3. Record contradictions or gaps across papers.',
        '4. Only after verification, move evidence into a formal manuscript.',
        '',
        '## Scientific Rule',
        'AI is an assistant, not a source. Never submit an AI-generated or placeholder claim without checking the original paper.',
        '',
        f'Generated on {day} by Daily Bioinformatics Paper Writer.'
    ]
    return '\n'.join(lines)

def main():
    cfg = json.load(open('config/topics.json', encoding='utf-8'))
    topic = cfg['topic']
    question = cfg['question']
    limit = int(cfg.get('papers', 20))
    years = int(cfg.get('years', 5))
    day = str(date.today())
    root = Path('output/daily') / day
    root.mkdir(parents=True, exist_ok=True)
    papers = root / 'papers'
    papers.mkdir(exist_ok=True)

    rows = search(topic, years, limit)
    json.dump(rows, open(root / 'literature.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    download_pdfs(rows, papers)

    # AI steps are optional — never allow them to stop PDF generation or emailing
    evidence = call('researcher', topic, question, rows)
    analysis = call('analyst', topic, question, {'papers': rows, 'researcher': evidence.get('text', '')})
    writer = call('writer', topic, question, {'papers': rows, 'analysis': analysis.get('text', '')})

    (root / 'researcher.md').write_text(evidence.get('text', ''), encoding='utf-8')
    (root / 'analysis.md').write_text(analysis.get('text', ''), encoding='utf-8')

    if writer.get('status') == 'ok' and writer.get('text') and 'LLM call failed' not in writer.get('text', '') and 'LLM not configured' not in writer.get('text', ''):
        review = writer['text']
    else:
        review = fallback_review(topic, question, rows)

    (root / 'review-paper.md').write_text(review, encoding='utf-8')
    review_pdf = root / 'review-paper.pdf'
    pdf(review_pdf, f'Daily Literature Review — {day}', review)

    # Keep a ZIP for the archive only (not emailed)
    zpath = root / f'collected-papers-{day}.zip'
    with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as z:
        for p in papers.glob('*.pdf'):
            z.write(p, p.name)

    email_log = []
    pdf_files = list(papers.glob('*.pdf'))

    # 1. Send the review PDF
    ok, msg = send(
        f'Daily Bioinformatics Research — Review PDF — {day}',
        f'Topic: {topic}\n\nResearch question: {question}\n\nPapers found: {len(rows)}\nOpen-access PDFs downloaded: {len(pdf_files)}\n\nThis email contains the literature-review PDF.\nIndividual paper PDFs will arrive in separate emails.\n\nAlways verify original papers before using any claims.',
        [str(review_pdf)]
    )
    email_log.append(f'review-paper.pdf: {msg}')

    # 2. Send one email per individual paper PDF
    for i, p in enumerate(sorted(pdf_files), 1):
        ok, msg = send(
            f'Daily Bioinformatics Research — Paper {i}/{len(pdf_files)} — {day}',
            f'Topic: {topic}\n\nThis is paper {i} of {len(pdf_files)} open-access PDFs collected today.\n\nFilename: {p.name}\n\nAlways verify the original source.',
            [str(p)]
        )
        email_log.append(f'{p.name}: {msg}')

    (root / 'email-status.txt').write_text('\n'.join(email_log), encoding='utf-8')
    success_count = sum(1 for line in email_log if line.endswith(': sent'))
    print(f'Completed: {day}; papers={len(rows)}; pdfs={len(pdf_files)}; emails_sent={success_count}/{len(email_log)}')

if __name__ == '__main__':
    main()
