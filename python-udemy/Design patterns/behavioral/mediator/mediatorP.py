"""
Mediator é um padrão de projeto comportamental
que tem a intenção de definir um objeto que encapsula 
a forma como um conjunto de objetos interage. O
Mediator promove o baixo acoplamento ao evitar que os 
objetos se refiram uns aos outros explicitamente e 
permite variar sua interações independentemente.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Colleague(ABC):
    def __init__(self, name) -> None:
        self.name = name
    
    @abstractmethod
    def broadcast(self, msg: str) -> None: pass
    
    @abstractmethod
    def direct(self, msg: str) -> None: pass
    
    
class Person(Colleague):
    def __init__(self, name: str, mediator: Mediator) -> None:
        self.name = name
        self.mediator = mediator
        
        
    def broadcast(self, msg: str) -> None:
        self.mediator.broadcast(self, msg)
        
        
    def send_direct(self, receiver: str, msg: str) -> None:
        self.mediator.direct(self, receiver, msg)
        
        
    def direct(self, msg: str) -> None:
        print(msg)
        
        
class Mediator(ABC):
        
    @abstractmethod
    def broadcast(self, colleague: Colleague, msg: str) -> None: pass     
        
    
    
    @abstractmethod
    def direct(self, sender: Colleague, receiver: str, msg: str) -> None: pass    


class ChatRoom(Mediator):
    def __init__(self) -> None:
        self.colleagues: List[Colleague] = []
        
        
    def is_colleague(self, colleague: Colleague) -> bool:
        return colleague in self.colleagues 
        
        
    def add(self, colleague: Colleague) -> None:
        if not self.is_colleague(colleague):
            self.colleagues.append(colleague)
            
        
    def remove(self, colleague: Colleague) -> None:
        if self.is_colleague(colleague):
            self.colleagues.remove(colleague)
            
            
    def broadcast(self, colleague: Colleague, msg: str) -> None:
        if not self.is_colleague(colleague):
            return 
        
        print(f'{colleague.name} disse: {msg}')
       
        
    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:
        if not self.is_colleague(sender):
            return
        
        receiver_obj: List[Colleague] = [
            colleague for colleague in self.colleagues
            if colleague.name == receiver
        ]
        
        if not receiver_obj:
            return
        
        receiver_obj[0].direct(
            f'{sender.name} para {receiver_obj[0].name}: {msg}'
        )
        
        
if __name__ == "__main__":
    chat = ChatRoom()
    
    vinicius = Person('Vinicius', chat)
    joana = Person('Joana', chat)
    jason = Person('Jason', chat)
    marcos = Person('Marcos', chat)
    viktor = Person('Viktor', chat)
    
    chat.add(vinicius)
    chat.add(joana)
    chat.add(jason)
    chat.add(marcos)
    
    vinicius.broadcast('Olá mundo.')
    joana.broadcast('Tudo bem com vocês?')
    viktor.broadcast("Olá")
    
    print()
    
    vinicius.send_direct('Joana', 'Olá Joana, tudo bem com você?')
    joana.send_direct('Vinicius', 'Sim, estou ótima...')
    
    
    
    