from fpdf import FPDF


class PDFReport:
    """
    PDF file that displays how much each roommate owes for the billing period.
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, roommates, bill):
        """
        Generates a pdf file detailing how much each roommate owes for the
        billing period
        :param roommates: the list of roommates
        :param bill: the bill
        :return:
        """
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        pdf.set_font(family='Arial', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Roommates Bill", border=1, align='C', ln=1)
        pdf.cell(w=100, h=40, txt="Period", border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        pdf.output(f"{self.filename}.pdf")
    