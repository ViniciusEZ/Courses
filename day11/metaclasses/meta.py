"""
Em PYTHON TUDO É UM OBJETO! Incluindo classes.
METACLASSES são as 'classes' que criam classes.
type é uma metaclasse.
"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        if 'attr_class' in namespace:
            del namespace['attr_class']
        # if 'talk1' not in namespace:
        #     print(f'O método "talk1" precisa ser criado na classe {name}')
        # else:
        #     if not callable(namespace['talk1']):
        #         print(f'Talk1 needs to be a method, not attr in {name}')
        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr_class = 'Value A'


class B(A):
    attr_class = 'Value B'


class C(B):
    attr_class = 'Value C'


b = B()
c = C()
print(b.attr_class)
print(c.attr_class)


class Father():
    name = 'NOME'


D = type('D',
         (Father,),
         {'attr': 'Hello World!'})
d = D()
print(d.attr)
print(type(d))
print(d.name)


def func() -> list | dict:
    return []
