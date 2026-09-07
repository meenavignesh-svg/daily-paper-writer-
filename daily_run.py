import os, json, zipfile, smtplib
from pathlib import Path
from email.message import EmailMessage
from datetime import date
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from agents.researcher import collect, download_open_access_pdfs
from agents.analyst import analyze
from agents.writer import write_review

ROOT=Path(__file__).parent
OUT=ROOT/"output"/"daily"/str(date.today()); OUT.mkdir(parents=True,exist_ok=True)
MAN=ROOT/"manuscript"; MAN.mkdir(exist_ok=True)


def md_pdf(text,path,title):
    styles=getSampleStyleSheet(); doc=SimpleDocTemplate(str(path),pagesize=A4,rightMargin=45,leftMargin=45,topMargin=45,bottomMargin=45)
    story=[Paragraph(title,styles['Title']),Spacer(1,14)]
    for raw in text.splitlines():
        line=raw.strip()
        if not line: story.append(Spacer(1,7)); continue
        if line.startswith('# '): story.append(Paragraph(line[2:],styles['Title']))
        elif line.startswith('## '): story.append(Paragraph(line[3:],styles['Heading2']))
        elif line.startswith('### '): story.append(Paragraph(line[4:],styles['Heading3']))
        else: story.append(Paragraph(line.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;'),styles['BodyText']))
        story.append(Spacer(1,5))
    doc.build(story)


def send_email(subject, body, attachments):
    host=os.getenv('SMTP_HOST'); port=int(os.getenv('SMTP_PORT','587')); user=os.getenv('SMTP_USERNAME'); password=os.getenv('SMTP_PASSWORD'); sender=os.getenv('EMAIL_FROM') or user; recipient=os.getenv('EMAIL_TO')
    if not all([host,user,password,sender,recipient]): return 'Email not configured: add SMTP_HOST, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, EMAIL_FROM, EMAIL_TO as GitHub Actions secrets.'
    msg=EmailMessage(); msg['Subject']=subject; msg['From']=sender; msg['To']=recipient; msg.set_content(body)
    for p in attachments:
        data=Path(p).read_bytes(); msg.add_attachment(data,maintype='application',subtype='pdf',filename=Path(p).name)
    with smtplib.SMTP(host,port,timeout=60) as s:
        s.starttls(); s.login(user,password); s.send_message(msg)
    return 'Email sent.'


def main():
    cfg=json.loads((ROOT/'config'/'topics.json').read_text())
    topic=cfg['topic']; question=cfg['research_question']; years=int(cfg.get('years_back',5)); limit=int(cfg.get('papers_per_database',20))
    papers=collect(topic,date.today().year-years,limit)
    papers=download_open_access_pdfs(papers,OUT/'papers')
    pd.DataFrame(papers).to_csv(OUT/'literature.csv',index=False)
    (OUT/'references.bib').write_text('\n\n'.join(f"@article{{paper{i}, title={{{p['title']}}}, author={{{p.get('authors','')}}}, year={{{p.get('year','')}}}, journal={{{p.get('journal','')}}}, doi={{{p.get('doi','')}}}, url={{{p.get('url','')}}}}}" for i,p in enumerate(papers,1)),encoding='utf-8')
    analysis=analyze(topic,question,papers)
    (OUT/'analysis.json').write_text(json.dumps(analysis,indent=2),encoding='utf-8')
    review=write_review(topic,question,papers,analysis)
    review_md=OUT/'review-paper.md'; review_md.write_text(review,encoding='utf-8')
    review_pdf=OUT/'review-paper.pdf'; md_pdf(review,review_pdf,f'Daily Review Paper — {date.today()}')
    (MAN/'manuscript.md').write_text(review,encoding='utf-8'); md_pdf(review,MAN/'manuscript.pdf','Accumulating Review Manuscript')
    pdfs=list((OUT/'papers').glob('*.pdf'))
    bundle=OUT/f'paper-pdfs-{date.today()}.zip'
    with zipfile.ZipFile(bundle,'w',zipfile.ZIP_DEFLATED) as z:
        z.write(review_pdf,review_pdf.name)
        for p in pdfs: z.write(p,f'papers/{p.name}')
    body=f'''Daily Bioinformatics Paper Writer — {date.today()}\n\nTopic: {topic}\nNew/collected records: {len(papers)}\nOpen-access PDFs downloaded: {len(pdfs)}\n\nAI pipeline: Researcher → Analyst → Writer\n\nThe attached ZIP contains the review-paper PDF plus every collected paper for which a confirmed open-access PDF could be legally downloaded. Papers without an OA PDF are listed in literature.csv but are not bypassed or scraped from paywalls.\n\nThe review is an AI-assisted draft and MUST be checked against the original papers before submission.'''
    # Email one ZIP rather than dozens of attachments to avoid mail attachment limits.
    send_email(f'Daily Research Package — {date.today()}',body,[bundle])
    print(body); print(f'Package: {bundle}')

if __name__=='__main__': main()
