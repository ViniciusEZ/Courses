from day5 import data
from data import products, people, list1
#
# for product in products:
#     print(product['preco'])

# def increase_price(p):
#     p['preco'] = round(p['preco'] * 1.05, 2)
#     return p
#
# new_products = map(increase_price, products)
#
# for product in new_products:
#     print(product)
# for p in people:
#     print(p)

def increase_age(p1):
    p1['age'] = p1['age'] + 10
    return p1

name = map(increase_age, people)
for people in name:
    print(people)