from abc import ABC, abstractmethod



class Account(ABC):
    regex = re.compile(r'^[0-9]+$')

    def __init__(self, agency, account, balance):
        self._agency = agency
        self._account = account
        self._balance = balance

    @property
    def agency(self):
        return self._agency

    @property
    def account(self):
        return self._account

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int | float)):
            raise ValueError('Balance needs to be numeric')
        self._balance = value

    def deposit(self, value):
        if not isinstance(value, (int | float)):
            raise ValueError('Deposit amount must be numeric.')
        self._balance += value
        self.detail()

    def detail(self):
        print(f'Agency: {self._agency},', end=' ')
        print(f'Account: {self._account},', end=' ')
        print(f'Balance: {self._balance}')

    @abstractmethod
    def withdraw(self, value):
        pass
