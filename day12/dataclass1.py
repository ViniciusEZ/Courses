"""
O que são dataclasses? O módulo dataclasses fornece
um decorador e funções para criar automaticamente métodos, como __init__(),
__repr__(), __eq__(), etc. Basicamente, Dataclasses são syntax sugar para criar
classes normais.
"""

from dataclasses import dataclass, asdict, astuple
from dataclasses import field


@dataclass(eq=True, repr=True, order=True, frozen=False, init=True)
class Person:
    name: str
    lastname: str = field(repr=False)

    def __post_init__(self):
        if not isinstance(self.name, str):
            raise TypeError(f'Invalid type {type(self.name).__name__} != str em {self}')

    @property
    def full_name(self):
        return f'{self.name} {self.lastname}'


p1 = Person('A', '5')
p2 = Person('B', '3')
p3 = Person('D', '4')
p4 = Person('C', '1')
people = [p1, p2, p3, p4]
print(sorted(people, key=lambda x: x.lastname))
print(p1)
print(p1 == p2)
print(asdict(p1))
print(astuple(p2))


# print(p1.name)
# print(p1.lastname)
# print(p1.fullname)
