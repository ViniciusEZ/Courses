from day11.exercise_classes.accs.account import *


class CheckingAccount(Account):
    def __init__(self, agency, accountnumber, balance, limit=100):
        super().__init__(agency, accountnumber, balance)
        self.limit = limit

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, value):
        if not isinstance(value, int | float):
            raise ValueError('Limit needs to be a numeric value.')
        self._limit = value

    def withdraw(self, value):
        if value > (self._balance + self._limit):
            print('Insufficient balance')
            return
        self._balance -= value
        self.show_details()


