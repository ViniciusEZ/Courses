"""
O proxy é um padrão de projeto comportamental que tem
a intenção de fornecer um objeto substituto que atua
como se fosse o objeto real que o código cliente
gostaria de usar.
O proxy receberá as solicitalções e terá controle
sobre como e quando repassar tais solicitações ao
objeto real.

Com base no modo como os proxies são usados,
nós os classificamos como:
- Proxy Virtual: controle acesso a recursos que podem
ser caros para criação ou utilização.

- Proxy Remoto: controla acesso a recursos que estão
em servidores remotos.

- Proxy de proteção: controla acesso a recursos que
possam necessitar autenticação ou permissão.

- Proxy Inteligente: além de controlar acesso ao
objeto real, também executa tarefas adicionais para
saber quando e como executar deteminadas ações.

Proxies podem fazer várias coisas:
criar logs, autenticar usuários, distribuir serviços,
criar cache, criar e destruir objetos, adiar execuções
e muito mais...
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep
from typing import List, Dict

class IUser(ABC):
    """ Subject Interface """
    firstname: str
    lastname: str
    
    @abstractmethod
    def get_addresses(self) -> List[Dict]: pass
    
    @abstractmethod
    def get_all_user_data(self) -> Dict: pass
    
    
class RealUser(IUser):
    """ Real Subject """
    def __init__(self, firstname: str, lastname: str) -> None:
        sleep(2) # Simulando requisição
        self.firstname = firstname
        self.lastname = lastname
    
    def get_addresses(self) -> List[Dict]:
        sleep(2)
        return [
            {'rua': 'Av. Margarete da Cruz', 'numero': 220}
        ]
    
    def get_all_user_data(self) -> Dict:
        sleep(2)
        return {'cpf': '222.222.222-22', 
                'rg': '43.657.891-1'}
        
class UserProxy(IUser):
    """ Proxy """
    
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        
        # Ainda não existem nesse ponto do código.
        self._real_user: RealUser
        self._cached_adresses: List[Dict]
        self._all_user_data: Dict
        
    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
           self._real_user = RealUser(self.firstname, self.lastname)
           
    
    def get_addresses(self) -> List[Dict]:
        self.get_real_user()
        
        if not hasattr(self, '_cached_adresses'):
           self._cached_adresses = self._real_user.get_addresses()
           
        return self._cached_adresses

    
    def get_all_user_data(self) -> Dict:
        self.get_real_user()
        
        if not hasattr(self, '_all_user_data'):
           self._all_user_data = self._real_user.get_all_user_data()
           
        return self._all_user_data
    
    
if __name__ == "__main__":
    vinicius = UserProxy('Vinicius', 'Ezequiel')
    
    print(vinicius.firstname)
    print(vinicius.lastname)
    
    # 6 sec
    print(vinicius.get_all_user_data())
    print(vinicius.get_addresses())
    
    print('Cached data: ')
    # Instant response
    for i in range(10):
        print(vinicius.get_addresses())