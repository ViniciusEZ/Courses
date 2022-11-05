class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join([f'{k}={v}' for k,v in self.__dict__.items()])
        return f'{self.__class__.__name__} ({params})'
    
    def __repr__(self) -> str:
        return self.__str__()


class Monostate(StringReprMixin):
    _state = {}
    
    def __new__(cls, *args, **kwargs):
        obj =  super().__new__(cls)
        obj.__dict__ = cls._state
        return obj
    
    
    def __init__(self, name=None, lastname=None):
        if name is not None:
            self.name = name
            
        if lastname is not None:
            self.lastname = lastname
            
class A(Monostate):
    pass
        
        
if __name__ == "__main__":
    m1 = Monostate('Vinicius')
    m2 = A(lastname='Kano')
    print(m1)
    print(m2)
    
    
    
        
        
