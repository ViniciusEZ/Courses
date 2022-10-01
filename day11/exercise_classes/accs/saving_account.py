from day11.exercise_classes.accs.account import *


class SavingAccount(Account):
    def withdraw(self, value):
        if value > self._balance:
            print('Insufficient balance')
            return
        self._balance -= value
        self.show_details()





