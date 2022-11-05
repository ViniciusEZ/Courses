"""
Singleton tem a intenção de garantir que uma classe tenha somente
uma instância e que forneça um ponto global de acesso para a mesma.
"""


class AppSettings:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        self.tema = 'O tema escuro'
        self.font = '20px'
    
if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = 'O tema verde'
    
    print(as1.tema)
    
    as2 = AppSettings()
    print(as1.tema)
    
    

