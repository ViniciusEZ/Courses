class Singleton(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self):
        self.tema = 'O tema escuro'
        self.font = '20px'
    
if __name__ == "__main__":
    as1 = AppSettings()
    as2 = AppSettings()
    as1.tema = 'O tema amarelo'
    print(as1.tema)
    print(as2.tema)
    





















#class Meta(type):
#    def __call__(cls, *args, **kwargs):
#        return super().__call__(*args, **kwargs)


#class Person(metaclass=Meta):
#    def __new__(cls, *args, **kwargs):
#        return super().__new__(cls)
    
    
#    def __init__(self, name):
#        self.name = name
    
        
#    def __call__(self, *args):
#        print('Oi')
    
    
#p1 = Person("Vinicius")
#p1()