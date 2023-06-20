class Bill:
    """
    Object that contains data about a bill, including total amount and billing
    period.
    """
    def __init__(self, amount, period):
        self.period = period
        self.amount = amount
        