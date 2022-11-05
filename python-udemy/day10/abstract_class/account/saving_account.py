from day10.abstract_class.account.bank_account import Account


class SavingAccount(Account):
    def withdraw(self, value):
        if value > self._balance:
            print('Insufficient balance.')
            return
        self._balance -= value
        self.detail()


