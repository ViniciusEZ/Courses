from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency, account, balance):
        self._agency = agency
        self._account = account
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int | float)):
            raise ValueError('Balance needs to be a numeric value.')
        self._balance = value

    @property
    def account(self):
        return self._account

    @property
    def agency(self):
        return self._agency

    def show_details(self):
        print(f'AGENCY: {self._agency} |ACCOUNT NUMBER: {self._account}|BALANCE: {self.balance}')

    def deposit(self, value):
        if not isinstance(value, int | float):
            raise ValueError('Deposit value needs to be numeric.')
        self._balance += value
        self.show_details()

    @abstractmethod
    def withdraw(self, value):
        pass
