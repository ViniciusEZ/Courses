"""
Polirmorfismo é o princípio que permite que classes derivadas de uma mesma
superclasse tenham métodos iguais (de mesma assinatura) mas comportamentos
diferentes.
Mesma assinatura = Mesma quantidade e tipo de parâmetros.
"""
from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def talk(self, msg):
        ...


class B(A):
    def talk(self, msg):
        print(f'B is speaking about {msg}')


class C(A):
    def talk(self, msg):
        print(f'C is speaking about {msg}')


b = B()
c = C()

b.talk('FOOD')
c.talk('VIDEOGAMES')
