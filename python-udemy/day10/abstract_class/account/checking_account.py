from day10.abstract_class.account.bank_account import Account


class CheckingAccount(Account):
    def __init__(self, agency, account, balance, limit=100):
        super().__init__(agency, account, balance)
        self._limit = limit

    @property
    def limit(self):
        return self._limit

    def withdraw(self, value):
        if value > (self._balance + self._limit):
            print('Insufficient balance.')
            return
        self._balance -= value
        self.detail()


