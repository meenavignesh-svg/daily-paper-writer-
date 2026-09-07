import os
import smtplib
from email.message import EmailMessage
from pathlib import Path

def send(subject, body, attachments):
    host = os.getenv("SMTP_HOST")
    port = int(os.getenv("SMTP_PORT", "587"))
    user = os.getenv("SMTP_USERNAME")
    password = os.getenv("SMTP_PASSWORD")
    sender = os.getenv("EMAIL_FROM") or user
    recipient = os.getenv("EMAIL_TO")

    missing = [name for name, val in [
        ("SMTP_HOST", host),
        ("SMTP_USERNAME", user),
        ("SMTP_PASSWORD", password),
        ("EMAIL_FROM / SMTP_USERNAME", sender),
        ("EMAIL_TO", recipient),
    ] if not val]

    if missing:
        return False, f"Email secrets not configured: {', '.join(missing)}"

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient
    msg.set_content(body)

    for path in attachments:
        p = Path(path)
        if not p.exists():
            continue
        data = p.read_bytes()
        subtype = "pdf" if p.suffix.lower() == ".pdf" else "zip" if p.suffix.lower() == ".zip" else "octet-stream"
        msg.add_attachment(data, maintype="application", subtype=subtype, filename=p.name)

    try:
        with smtplib.SMTP(host, port, timeout=60) as smtp:
            smtp.starttls()
            smtp.login(user, password)
            smtp.send_message(msg)
        return True, "sent"
    except smtplib.SMTPAuthenticationError:
        return False, "Gmail authentication failed. Use an App Password (not your normal password) and ensure 2-Step Verification is enabled."
    except Exception as e:
        return False, f"Email send failed: {e}"
