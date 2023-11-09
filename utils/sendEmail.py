import os
from email.message import EmailMessage
import ssl
import smtplib


def send_mail(send_to, pdf_filename):
    email_sender = "sojitrapreet0307@gmail.com"
    email_password = "fepp oqzt xxbl kdco"
    email_receiver = send_to

    subject = "Your movie script is ready!"
    body = "Hi there, please find attached your movie script."
    em = EmailMessage()

    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)

    # Add the PDF attachment
    with open(pdf_filename, "rb") as pdf:
        em.add_attachment(
            pdf.read(),
            maintype="application",
            subtype="pdf",
            filename=os.path.basename(pdf_filename),
        )

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email_receiver, em.as_string())
        print("Email Sent")
