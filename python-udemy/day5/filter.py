from day5 import data
from data import products, people, list1


def filtra(p):
    if p['preco'] > 50:
        return True
    else:
        return False

new_list = filter(filtra, products)
for product in new_list:
    print(product)