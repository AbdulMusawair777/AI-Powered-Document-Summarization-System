from fpdf import FPDF

def export_txt(summary):

    with open("output/summary.txt",
              "w",
              encoding="utf-8") as f:

        f.write(summary)


def export_pdf(summary):

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, summary)

    pdf.output("output/summary.pdf")