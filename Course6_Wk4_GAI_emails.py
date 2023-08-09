#!/usr/bin/env python3

import smtplib
from email.message import EmailMessage

def generate_email(sender, recipient, subject, body, attachment=None):
    message = EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    if attachment:
        with open(attachment, "rb") as f:
            attachment_data = f.read()
            attachment_name = attachment.split("/")[-1]
            message.add_attachment(attachment_data, maintype="application", subtype="octet-stream", filename=attachment_name)

    return message

def send_email(message):
    smtp_server = "localhost"

    try:
        server = smtplib.SMTP(smtp_server)
        server.starttls()
        server.send_message(message)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print("Error sending email:", e)
