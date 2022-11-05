from day11.exercise_classes.Client.Person import Person


class Client(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._account = None

    def insert_account(self, account):
        self._account = account

    @property
    def account(self):
        return self._account
