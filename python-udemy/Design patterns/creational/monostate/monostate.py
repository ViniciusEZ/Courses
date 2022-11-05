"""
Monostate (ou Borg) - É uma variação do Singleton proposto
por Alex Martelli que tem a intenção de garantir que o estado
do objeto seja igual para todas as instâncias.
"""


class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join([f'{k}={v}' for k,v in self.__dict__.items()])
        return f'{self.__class__.__name__} ({params})'
    
    def __repr__(self) -> str:
        return self.__str__()


class MonostateSimple(StringReprMixin):
    _state = {}
    
    
    def __init__(self, name=None, lastname=None):
        self.__dict__ = self._state
        
        if name is not None:
            self.name = name
            
        if lastname is not None:
            self.lastname = lastname
        
        
if __name__ == "__main__":
    m1 = MonostateSimple('Vinicius')
    m2 = MonostateSimple(lastname='Ezequiel')
    print(m1)
    print(m2)
        
    
        
        
