"""
Template Method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos 
para as subclasses por herança. Template Method permite que subclasses redefinam
certos passos de um algoritmo sem mudar a estrutura do mesmo.

Também é possível definir hooks para que as subclasses utilizem
caso necessário.

The Hollywood principle: "Don't Call Us, We'll Call You."
(IoC - Inversão de controle)
"""

from abc import ABC, abstractmethod


class Abstract(ABC):
    def template_method(self):
        self.hook()
        self.operation1()
        self.base_class_method()
        self.operation2()
      
        
    def base_class_method(self):
        print('Eu sou da classe abstrata...')
    
    
    def hook(self): pass
    
    
    @abstractmethod
    def operation1(self): pass
    
    
    @abstractmethod
    def operation2(self): pass
    
    
class ConcreteClass(Abstract):
    def hook(self):
        print('Hook utilizado...')
    
    def operation1(self):
        print('Operação 1 concluída...')
    
      
    def operation2(self):
        print('Operação 2 concluída...')
        
class ConcreteClass2(Abstract):
    def operation1(self):
        print('Operação 1 (diferente) concluída...')
    
      
    def operation2(self):
        print('Operação 2 (diferente) concluída...')
        
        
if __name__ == "__main__":
    c1 = ConcreteClass()
    c2 = ConcreteClass2()
    
    
    c1.template_method() 
    print()
    c2.template_method() 