"""
Javascript Object Notation - JSON
JSON é um formato de troca de dados entre sistemas e programas muito
leve e de fácil utilização. Muito utilizados por APIs.
"""

from datas import *
import json

with open('clients.json', 'r') as file:
    datas = json.load(file)
    print(datas)
    # json.dump(dict_clients, file, indent=4)

for k, v in datas.items():
    print(f'{k} - {v}')

# dicts = json.loads(json_clients)
# for k, v in dicts.items():
#     print(f'{k} - {v}')
#


# datas_json = json.dumps(dict_clients, indent=True)
# print(datas_json)


# lista = [1,2,3,4,5,6]
# datas_json = json.dumps(lista)
# print(datas_json)
