import os, smtplib, zipfile, json
from email.message import EmailMessage
from pathlib import Path

def send(subject, body, attachments):
    host=os.getenv('SMTP_HOST'); port=int(os.getenv('SMTP_PORT','587')); user=os.getenv('SMTP_USERNAME'); password=os.getenv('SMTP_PASSWORD'); sender=os.getenv('EMAIL_FROM') or user; recipient=os.getenv('EMAIL_TO')
    if not all([host,user,password,sender,recipient]): return False, 'Email secrets not configured'
    msg=EmailMessage(); msg['Subject']=subject; msg['From']=sender; msg['To']=recipient; msg.set_content(body)
    for path in attachments:
        p=Path(path)
        if not p.exists(): continue
        data=p.read_bytes(); msg.add_attachment(data,maintype='application',subtype='pdf' if p.suffix.lower()=='.pdf' else 'zip',filename=p.name)
    with smtplib.SMTP(host,port,timeout=60) as smtp:
        smtp.starttls(); smtp.login(user,password); smtp.send_message(msg)
    return True, 'sent'
