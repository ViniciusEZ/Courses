from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def talk(self):
        pass


class B(A):
    def talk(self):
        print('Talking...B')


b = B()
b.talk()