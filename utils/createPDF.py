from fpdf import FPDF
import os


def createPDF(title, text, output_filename, destination="F"):
    # make "pdfs" directory in the root directory if it doesn't exist
    if not os.path.exists("pdfs"):
        os.mkdir("pdfs")

    # make "tmp_pdfs" directory in the root directory if it doesn't exist. This temp_pdfs directory is used to store the pdfs temporarily so that they can be sent to the user via email.
    if not os.path.exists("tmp_pdfs"):
        os.mkdir("tmp_pdfs")

    # print("Creating PDF...")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=16)
    title_width = pdf.get_string_width(title)
    x_title = (pdf.w - title_width) / 2
    pdf.cell(200, 10, txt=title, ln=True, align="C")
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=text, align="J")
    pdf.output(output_filename, dest=destination)
