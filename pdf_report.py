import webbrowser

from fpdf import FPDF


class PDFReport:
    """
    PDF file that displays how much each roommate owes for the billing period.
    """
    def __init__(self, filename):
        self.filename = f"{filename}.pdf"

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
        pdf.image("house.png", w=50, h=50)

        pdf.set_font(family='Arial', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Roommates Bill", border=1, align='C', ln=1)

        pdf.set_font(family="Arial", size=18, style='B')
        pdf.cell(w=100, h=40, txt="Period", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        pdf.set_font(family="Arial", size=14)

        for roommate in roommates:
            amount_due = str(roommate.get_amount_to_pay(bill, roommates))
            pdf.cell(w=100, h=25, txt=roommate.name, border=0)
            pdf.cell(w=150, h=25,
                     txt=amount_due,
                     border=0,
                     ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)
    