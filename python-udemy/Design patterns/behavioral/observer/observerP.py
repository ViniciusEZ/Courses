"""
O padrão Observer tem a intenção de definir uma dependência
de um-para-muitos entre objetos, de maneira que quando um objeto muda
de estado, todos os seus dependentes são notificados e atualizados
automaticamente.

Um Observer é um objeto que gostaria de ser informado, um observable
(subject) é a entidade que gera as informações.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict


class IObservable(ABC):
    """Observable"""
    
    @property
    @abstractmethod
    def state(self): pass
        
    
    @abstractmethod
    def add_observer(self, observer: IObserver) -> None: pass
    
    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None: pass
    
    @abstractmethod
    def notify_observers(self) -> None: pass
    
    
class WeatherStation(IObservable):
    """Observable"""
    
    def __init__(self) -> None:
        self._observers: List[IObserver] = []
        self._state: Dict = {}
        
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, state_update: Dict) -> None:
        new_state: Dict = {**self._state, **state_update}
        
        if new_state != self._state:
            self._state = new_state
            self.notify_observers()     
            
    def reset_state(self):
        self._state = {}
        self.notify_observers()
    
    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(observer)
    
    def remove_observer(self, observer: IObserver) -> None:
        if observer not in self._observers:
            return
        
        self._observers.remove(observer)
    
    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()
        print()
            
            
class IObserver(ABC):
    @abstractmethod
    def update(self) -> None: pass
    
    
class SmarthPhone(IObserver):
    def __init__(self, name, observable: IObservable) -> None:
        self.name = name
        self.observable = observable
    
    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(f'{self.name} o objeto {observable_name} '
              f'acabou de ser atualizado -> {self.observable.state}')
        
        
class NoteBook(IObserver):
    def __init__(self, observable: IObservable) -> None:
        self.observable = observable
    
    def show(self):
        state = self.observable.state
        print('Sou o NoteBook.', state)
    
    def update(self) -> None:
        self.show()
        
        
if __name__ == "__main__":
    weather_station = WeatherStation()
    
    smartphone = SmarthPhone('MotoG', weather_station)
    outro_smartphone = SmarthPhone('IPhone', weather_station)
    notebook = NoteBook(weather_station)
    
    weather_station.add_observer(smartphone)
    weather_station.add_observer(outro_smartphone)
    weather_station.add_observer(notebook)
    
    weather_station.state = {'temperature': '30'}
    weather_station.state = {'temperature': '33', 'humidity': '90'}
    
    weather_station.remove_observer(outro_smartphone)
    weather_station.reset_state()