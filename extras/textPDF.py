import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import streamlit as st
from fpdf import FPDF


def createPDF(title, text, output_filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=16)
    title_width = pdf.get_string_width(title)
    x_title = (pdf.w - title_width) / 2
    pdf.cell(200, 10, txt=title, ln=True, align="C")
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=text, align="J")
    pdf.output(output_filename)


title = "Sample Title"
textToWrite = "This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. This is a sample text paragraph that will be saved as a PDF. You can replace this with your own text. "

pdf = "sample.pdf"


if st.button("Generate Pdf", type="primary"):
    createPDF(title, textToWrite, pdf)


# ****************************************************************************************************************


def sendEmail(pdf_file, recipient_email, sender_email, sender_password):
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = "Here's your Story"

    # Attach the PDF file
    with open(pdf_file, "rb") as attachment:
        part = MIMEApplication(attachment.read(), Name="sample.pdf")
    part["Content-Disposition"] = f'attachment; filename="{pdf_file}"'
    msg.attach(part)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)

    text = msg.as_string()
    server.sendmail(sender_email, recipient_email, text)

    server.quit()


pdf_file = "sample.pdf"
recipient_email = st.text_input("Enter recipient's email address: ")
sender_email = ""
sender_password = ""


if st.button("Send to given email address", type="primary"):
    sendEmail(pdf_file, recipient_email, sender_email, sender_password)
