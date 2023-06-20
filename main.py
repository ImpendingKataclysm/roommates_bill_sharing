from bill import Bill
from pdf_report import PDFReport
from roommate import Roommate

if __name__ == "__main__":
    # Get Bill data
    bill_amount_usd = float(input("Enter bill amount: "))
    bill_period = input("Enter the billing period: ")
    bill = Bill(bill_amount_usd, bill_period)

    # Get Roommate data
    roommates = []

    while True:
        roommate_name = input("Enter a roommate's name: ")
        roommate_days_home = int(input(f"How many days did they live here during {bill.period}? "))
        roommate = Roommate(roommate_name, roommate_days_home)

        roommates.append(roommate)

        add_another = input("Add another roommate? (Y/N) ").lower().strip()

        if add_another == 'n' or add_another == 'no':
            break

    print(f"Total due for {bill.period}: {bill.amount}")

    for roommate in roommates:
        print(f"{roommate.name} pays {roommate.get_amount_to_pay(bill, roommates)}")

    pdf_report = PDFReport(bill.period)
    pdf_report.generate(roommates, bill)
