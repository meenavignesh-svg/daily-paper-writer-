import os, json, zipfile, csv
from pathlib import Path
from datetime import date
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from agents.researcher import search, download_pdfs
from agents.ai import call
from agents.emailer import send

def pdf(path,title,text):
    styles=getSampleStyleSheet(); doc=SimpleDocTemplate(str(path),pagesize=A4,rightMargin=45,leftMargin=45,topMargin=45,bottomMargin=45); story=[Paragraph(title,styles['Title']),Spacer(1,12)]
    for block in text.split('\n'):
        if block.strip(): story.append(Paragraph(block.replace('&','&amp;'),styles['BodyText'])); story.append(Spacer(1,7))
    doc.build(story)

def main():
    cfg=json.load(open('config/topics.json',encoding='utf-8')); topic=cfg['topic']; question=cfg['question']; limit=int(cfg.get('papers',20)); years=int(cfg.get('years',5)); day=str(date.today()); root=Path('output/daily')/day; root.mkdir(parents=True,exist_ok=True); papers=root/'papers'; papers.mkdir(exist_ok=True)
    rows=search(topic,years,limit); json.dump(rows,open(root/'literature.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
    download_pdfs(rows,papers)
    evidence=call('researcher',topic,question,rows); analysis=call('analyst',topic,question,{'papers':rows,'researcher':evidence['text']}); writer=call('writer',topic,question,{'papers':rows,'analysis':analysis['text']})
    (root/'researcher.md').write_text(evidence['text'],encoding='utf-8'); (root/'analysis.md').write_text(analysis['text'],encoding='utf-8')
    review=writer['text']; (root/'review-paper.md').write_text(review,encoding='utf-8'); pdf(root/'review-paper.pdf',f'Daily Literature Review — {day}',review)
    zpath=root/f'collected-papers-{day}.zip'
    with zipfile.ZipFile(zpath,'w',zipfile.ZIP_DEFLATED) as z:
        for p in papers.glob('*.pdf'): z.write(p,p.name)
    attachments=[str(root/'review-paper.pdf'),str(zpath)]
    ok,msg=send(f'Daily Bioinformatics Research — {day}',f'Topic: {topic}\nNew records: {len(rows)}\nOpen-access PDFs downloaded: {len(list(papers.glob("*.pdf")))}\n\nThe review PDF and collected-paper ZIP are attached. Always verify original papers before submission.',attachments)
    (root/'email-status.txt').write_text(msg,encoding='utf-8')
    print(f'Completed: {day}; papers={len(rows)}; pdfs={len(list(papers.glob("*.pdf")))}; email={ok}')
if __name__=='__main__': main()
