class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.nameClass = self.__class__.__name__

    def talk(self):
        print(f'{self.name} is talking')


class Client(Person):
    def buy(self):
        print(f'{self.name} is buying')

    def talk(self):
        print("I'm Client")


class VipClient(Client):
    def __init__(self, name, lastname, age):
        Person.__init__(self, name, age)
        self.lastname = lastname

    def fullname(self):
        return f'{self.name} {self.lastname}'

    def talk(self):
        Person.talk(self)
        Client.talk(self)
        print(f'{self.fullname()} is talking.')
