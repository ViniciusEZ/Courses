class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.nameClass = self.__class__.__name__

    def talk(self):
        print(f'{self.nameClass} is talking')


class Client(Person):
    def buy(self):
        print(f'{self.name} is buying')


class Student(Person):
    def study(self):
        print(f'{self.name} is studying')



