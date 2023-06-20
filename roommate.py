class Roommate:
    """
    Person who lives in the home and pays a share of the bills.
    """
    def __init__(self, name, days_home):
        self.days_home = days_home
        self.name = name

    def get_amount_to_pay(self, bill, roommates):
        """
        Calculates the amount this Roommate owes for the given bill based on
        how many days each roommate spent at home during the billing period.
        :param bill: the bill for which the period is calculated
        :param roommates: the list of Roommates living at the home
        :return: the amount this Roommate owes for the billing period
        """
        roommates_days_home = 0

        for roommate in roommates:
            roommates_days_home += roommate.days_home

        weight = self.days_home / roommates_days_home
        amount = bill.amount * weight

        return amount
