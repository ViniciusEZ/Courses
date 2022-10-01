'''
Combinations - Ordem não importa
Permutation - Ordem importa
Ambos não repetem valores únicos
Product - Ordem importa e repete valores únicos
'''
from itertools import permutations, combinations, product

people = ['Luiz', 'Andrè', 'Eduardo', 'Favero', 'Francisco', 'Jayce']

for group in product(people, repeat=2):
    print(group)