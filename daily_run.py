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
    lines = [
        f'# Daily Literature Review — {date.today()}',
        '',
        f'**Topic:** {topic}',
        f'**Research question:** {question}',
        '',
        '## Note',
        'AI drafting was unavailable or failed. This is a structured evidence list only. Always read the original papers before using any claims.',
        '',
        '## Papers',
        ''
    ]
    for i, r in enumerate(rows, 1):
        lines += [
            f'### [{i}] {r.get("title", "Untitled")}',
            f'- Year: {r.get("year", "")}',
            f'- Source: {r.get("source", "")}',
            f'- Authors: {r.get("authors", "")}',
            f'- DOI: {r.get("doi") or "Not supplied"}',
            f'- URL: {r.get("url", "")}',
            '- Key finding: **[READ AND VERIFY]**',
            '- Methods/dataset: **[EXTRACT]**',
            '- Limitation: **[EXTRACT]**',
            ''
        ]
    lines += [
        '## Researcher checklist',
        '- [ ] Read the original papers',
        '- [ ] Verify every claim and reference',
        '- [ ] Record methods, datasets and limitations',
        '- [ ] Add only evidence-supported statements to the manuscript'
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

    if writer.get('status') == 'ok':
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
        f'Topic: {topic}\n\nResearch question: {question}\n\nPapers found: {len(rows)}\nOpen-access PDFs downloaded: {len(pdf_files)}\n\nThis email contains only the generated literature-review PDF.\nIndividual paper PDFs will arrive in separate emails.\n\nAlways verify original papers before using any claims.',
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
