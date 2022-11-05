from abc import ABC, abstractmethod


class Pizza(ABC):
    def prepare(self) -> None: 
        """ Template method """
        self.hook_before_add_ingredients() # Hook
        self.add_ingredients() # Abstract
        self.hook_after_add_ingredients() # Hook
        self.cook() # Abstract
        self.cut() # Concrete
        self.serve() # Concrete
        
        
    def hook_before_add_ingredients(self) -> None: pass
    def hook_after_add_ingredients(self) -> None: pass
        
    def cut(self) -> None:
        print(f'{self.__class__.__name__}: Cortando pizza...')
        
    def serve(self) -> None:
        print(f'{self.__class__.__name__}: Servindo pizza...')
        
    
    @abstractmethod
    def add_ingredients(self) -> None: pass
    
    
    @abstractmethod
    def cook(self) -> None: pass
    
    
class AModa(Pizza):
    def add_ingredients(self) -> None:
        print(f'{self.__class__.__name__} - adicionando ingredientes: presunto, queijo e carne.')
    
    def cook(self) -> None:
        print(f'{self.__class__.__name__}: cozinhando por 45min no forno a lenha.')
    
    
class FourCheese(Pizza):
    def hook_before_add_ingredients(self) -> None:
        print(f'{self.__class__.__name__}: Coletando e cortando os queijos.')
    
    def add_ingredients(self) -> None:
        print(f'{self.__class__.__name__} - adicionando ingredientes: Provolone, Mozzarela, Cottage, Parmesão.')
    
    def cook(self) -> None:
        print(f'{self.__class__.__name__}: cozinhando por 30min no forno a elétrico.')    
        
        
if __name__ == "__main__":
    a_moda = AModa()
    a_moda.prepare()
    print()
    
    four_cheese = FourCheese()
    four_cheese.prepare()