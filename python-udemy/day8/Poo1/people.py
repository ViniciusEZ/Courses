from datetime import datetime


class People:
    curdate = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, name, age, eating=False, talking=False):
        self.name = name
        self.age = age
        self.eating = eating
        self.talking = talking

    def talk(self, subject):
        if self.eating:
            print(f'{self.name} cannot speak while eat.')
            return

        if self.talking:
            print(f'{self.name} is already speaking.')
            return

        print(f'{self.name} is talking about {subject}')
        self.talking = True

    def stop_talk(self):
        if not self.talking:
            print(f'{self.name} is not talking')
            return

        print(f'{self.name} stop talk.')
        self.talking = False

    def eat(self, food):
        if self.eating:
            print(f'{self.name} is already eating!')
            return

        if self.talking:
            print(f'{self.name} cannot speak while eat.')
            return

        print(f'{self.name} is eating {food}.')
        self.eating = True

    def stop_eat(self):
        if not self.eating:
            print(f'{self.name} is not eating!')
            return

        print(f'{self.name} stop eating.')
        self.eating = False

    def get_birth_date(self):
        return self.curdate - self.age
