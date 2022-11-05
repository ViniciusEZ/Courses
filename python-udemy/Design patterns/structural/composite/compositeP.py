"""
Composite é um padrão de projeto estrutural que permite que
você utilize a composição para criar objetos em estruturas
de árvores. O padrão permite aos clientes tratarem de maneira
uniforme objetos individuais (leaf) e composições de 
objetos (Composite).

IMPORTANTE: Só aplique este padrão em uma estrutura que possa
ser representada em formato hierárquico (árvore).

No padrão Composite, temos dois tipos de objetos:
Composite (que representa nós internos da árvore) e Leaf
que representa nós externos da árvore).

Objetos Composite são objetos mais complexos e com filhos.
Geralmente, eles delegam trabalho aos filhos usando um 
método em comum.

Objetos Leaf são objetos simples, da ponta e sem filhos.
Geralmente, são esses objetos que realizam o trabalho
real da aplicação.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class BoxStructure(ABC):
    """ Component """
    @abstractmethod
    def print_content(self) -> None: pass

    @abstractmethod
    def get_price(self) -> float: pass
    
    def add(self, child: BoxStructure) -> None: pass
    
    def remove(self, child: BoxStructure) -> None: pass  
    
    
class Box(BoxStructure):
    """ Composite """
    def __init__(self, name) -> None:
        self.name = name
        self._children: List[BoxStructure] = []

    
    def print_content(self) -> None:
        print(f'\n{self.name}:')
        
        for child in self._children:
            child.print_content()


    def get_price(self) -> float:
        return sum([
            child.get_price() for child in self._children
        ])
    
    
    def add(self, child: BoxStructure) -> None:
        self._children.append(child)
        
        
    def remove(self, child: BoxStructure) -> None:
        if child in self._children:
            self._children.remove(child)
            

class Product(BoxStructure):
    """ Price """
    
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price
    
    def print_content(self) -> None:
        print(f'Name: {self.name}, Price: {self.price}')


    def get_price(self) -> float:
        return self.price
    
    
if __name__ == "__main__":
    # Leaf
    shirt1 = Product('shirt1', 50.99)
    shirt2 = Product('shirt2', 100.89)
    shirt3 = Product('shirt3', 45.90)
    
    
    # Composite
    shirt_box = Box('shirt_box')
    shirt_box.add(shirt1)
    shirt_box.add(shirt2)
    shirt_box.add(shirt3)
    shirt_box.print_content()
    print(shirt_box.get_price())
    
    # Leaf
    smartphone1 = Product('smartphone1', 10000)
    smartphone2 = Product('smartphone2', 12500)
    
    print()
    # Composite
    phone_box = Box('phone_box') 
    phone_box.add(smartphone1)
    phone_box.add(smartphone2)
    phone_box.print_content()
    print(phone_box.get_price())
    print()
    # Composite
    big_box = Box('big_box')
    big_box.add(phone_box)
    big_box.add(shirt_box)
    big_box.print_content()
    print(big_box.get_price()) 