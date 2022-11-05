"""
Flyweight é um padrão de projeto estrutural
que tem a intenção de usar compartilhamento
para suportar eficientemente grandes quantidades
de objetos de forma granular.

Só use Flyweight quando TODAS as condições
a seguir forem verdadeiras:

- Uma aplicação utiliza uma grande quantidade de
objetos;
- Os custos de armazenamento são altos por causa
da grande quantidade de objetos;
- A maioria dos estados de objetos podem se tornar
extrínsecos;
- Muitos objetos podem ser substituídos por poucos
objetos compartilhados;
- A aplicação não deoende da identidade dos objetos.

IMPORTANTE:
- Estado intrínseco é o estado do objeto que não muda,
esse estado deve estar dentro do objeto Flyweight;
- Estado extrínseco é o estado do objeto que muda,
esse estado pode ser movido para fora do objeto
Flyweight.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict

class Client:
    """ Context """
    
    def __init__(self, name: str) -> None:
        self.name = name
        self._addresses: List = []
    
        # Extrinsic address data
        self.address_number: str    
        self.address_detail: str
        
    def add_address(self, address: Address) -> None:
        self._addresses.append(address)
        
    def list_addresses(self) -> None:
        for address in self._addresses:
            address.show_address(self.address_number, self.address_detail)
            
class Address:
    """ Flyweight """
    def __init__(self, street: str, neighbourhood: str, zip_code: str) -> None:
        self._street = street
        self._neighbourhood = neighbourhood
        self._zip_code = zip_code
        
    def show_address(self, address_number: str, address_detail: str) -> None:
        print(
            self._street,
            address_number,
            self._neighbourhood,
            address_detail,
            self._zip_code
        )
        
class AddressFactory:
    _addresses: Dict = {}
    
    def _get_key(self, **kwargs) -> str:
        return ''.join(kwargs.values())
    
    def get_address(self, **kwargs) -> Address:
        key = self._get_key(**kwargs)
        
        try:
            address_flyweight = self._addresses[key]
            print('Using an existing object.')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print('Creating a new object.')
            
        return address_flyweight
    
if __name__ == "__main__":
    address_factory = AddressFactory()
    
    a1 = address_factory.get_address(street='Maria Margarete',
                                    neighbourhood='Centro',
                                    zip_code='00000-220')
    
    a2 = address_factory.get_address(street='Maria Margarete',
                                    neighbourhood='Centro',
                                    zip_code='00000-220')
    
    vinicius = Client('Vinicius')
    vinicius.address_number = '120'
    vinicius.address_detail = 'Casa 171'
    vinicius.add_address(a1)
    vinicius.list_addresses()
    print()
    maria = Client('Maria')
    maria.address_number = '200A'
    maria.address_detail = 'AP 369'
    maria.add_address(a2)
    maria.list_addresses()
    
    print(a1 == a2)