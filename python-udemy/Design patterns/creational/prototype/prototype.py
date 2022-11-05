"""
Especificar os tipos de objetos a serem criados usando uma
instância-protótipo e criar novos objetos pela cópia
desse protótipo.
Quais objetos são copiados com o sinal de atribuição? 
"""

from copy import deepcopy


class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join([f'{k}={v}' for k,v in self.__dict__.items()])
        return f'{self.__class__.__name__} ({params})'
    
    def __repr__(self) -> str:
        return self.__str__()
    

class Person(StringReprMixin):
    def __init__(self, firstname, lastname) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addresses = []
        
    def add_address(self, address):
        self.addresses.append(address)
        
    
    def clone(self):
        return deepcopy(self)
        
        
    
        
class Address(StringReprMixin):
    def __init__(self, street, number) -> None:
        self.street = street
        self.number = number
        
         
         
if __name__ == '__main__':
    vinicius = Person('Vinicius', 'Ezequiel')
    endereco_vinicius = Address('Maria Margarete', '220')
    vinicius.add_address(endereco_vinicius)
    
    esposa_vinicius = vinicius.clone()
    esposa_vinicius.firstname = 'Catarina'
    
    print(vinicius)
    print(esposa_vinicius)

