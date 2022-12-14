"""
Decorator é um padrão de projeto estrutural que permite que você
adicione novos comportamentos em objetos ao colocá-los dentro de
um "wrapper" (decorador) de objetos.
Decoradores fornecem uma alternativa flexível ao uso de subclasses
para a extensão de funcionalidades.

Decorator (padrão de projeto) != Decorator em Python

Python decorator -> Um decorator é um callable que aceita outra
função como argumento (a função decorada). O decorator pode
realizar algum processamento com a função decorada e devolvê-la
ou substituí-la por outra função ou objeto invocável.
Do livro "Python Fluente", de Luciano Ramalho (pág. 223)
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import List
from copy import deepcopy

# INGREDIENTS
@dataclass
class Ingredient:
    price: float
    
    
@dataclass
class Bread(Ingredient):
    price: float = 0.60
    
@dataclass
class Sausage(Ingredient):
    price: float = 5.00
    
@dataclass
class Bacon(Ingredient):
    price: float = 7.99
    
@dataclass
class Egg(Ingredient):
    price: float = 1.50
    
@dataclass
class Cheese(Ingredient):
    price: float = 6.79
    
@dataclass
class MashedPotatoes(Ingredient):
    price: float = 2.50


@dataclass
class PotatoSticks(Ingredient):
    price: float = 0.99


# HOTDOGS
class HotDog:
    _name: str
    _ingredients: List[Ingredient]
    
    @property
    def price(self) -> float:
        return round(sum(
            [ingredient.price for ingredient in self._ingredients]
            ), 2)
    
    @property
    def name(self) -> str:
        return self._name 
    
    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients
    
    def __repr__(self) -> str:
        return f'{self.name} ({self.price}) -> {self.ingredients}'
    
    
class SimpleHotDog(HotDog):
    def __init__(self) -> None:
        self._name = 'SimpleHotDog'
        self._ingredients: List[Ingredient] = [
            Bread(), Sausage(), PotatoSticks(),
            
            
        ]
        
class SpecialHotDog(HotDog):
    def __init__(self) -> None:
        self._name = 'SpecialHotDog'
        self._ingredients: List[Ingredient] = [
            Bread(), Sausage(), Bacon(), Egg(),
            Cheese(), MashedPotatoes(), PotatoSticks(),
        ]
        
# Decorators
class HotDogDecorator(HotDog):
    def __init__(self, hotdog: HotDog) -> None:
        self.hotdog = hotdog
        
    @property
    def price(self) -> float:
        return self.hotdog.price
    
    @property
    def name(self) -> str:
        return self.hotdog.name
    
    @property
    def ingredients(self) -> List[Ingredient]:
        return self.hotdog.ingredients

class BaconDecorator(HotDogDecorator):
    def __init__(self, hotdog: HotDog) -> None:
        super().__init__(hotdog)
        self._ingredient = Bacon()
        self._ingredients = deepcopy(self.hotdog.ingredients)
        self._ingredients.append(self._ingredient)
        
        
    @property
    def price(self) -> float:
        return round(sum(
            [ingredient.price for ingredient in self._ingredients]
            ), 2)
    
    @property
    def name(self) -> str:
        return f'{self.hotdog.name} + {self._ingredient.__class__.__name__}'
    
    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients
    
    

        
if __name__ == "__main__":
    simple_hotdog = SimpleHotDog()
    decorated_simple_hotdog = HotDogDecorator(simple_hotdog)
    bacon_simple_hotdog = BaconDecorator(simple_hotdog)
    bacon_simple_hotdog = BaconDecorator(bacon_simple_hotdog)
    
    print(simple_hotdog)
    print(decorated_simple_hotdog)
    print(bacon_simple_hotdog)
    
    