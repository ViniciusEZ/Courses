from random import randint

class Person:
    curdate = 2022

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_birth_date(self):
        print(self.curdate - self.age)

    @classmethod
    def birth_date(cls, name, birth_date):
        age = cls.curdate - birth_date
        return cls(name, age)

    @staticmethod
    def id_generator():
        return randint(10000, 19999)


# p1 = Person.birth_date('Vinicius', 2003)
p1 = Person('VInicius', 19)
print(p1)
print(p1.name, p1.age)
p1.get_birth_date()
print(Person.id_generator())
print(p1.id_generator())
