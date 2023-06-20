from bill import Bill
from pdf_report import PDFReport
from roommate import Roommate

if __name__ == "__main__":
    bill = Bill(120, "June 2023")
    roommates = []
    roommate1 = Roommate("John", days_home=20)
    roommate2 = Roommate("Mary", days_home=25)
    roommate3 = Roommate("Joe", days_home=28)

    roommates.append(roommate1)
    roommates.append(roommate2)
    roommates.append(roommate3)

    print(bill.amount, bill.period)

    for roommate in roommates:
        print(roommate.name, roommate.days_home)
        print(roommate.get_amount_to_pay(bill, roommates))

    pdf_report = PDFReport(bill.period)
    pdf_report.generate(roommates, bill)
