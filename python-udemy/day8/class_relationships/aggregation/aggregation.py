from functools import reduce


class Shoppingcart:
    def __init__(self):
        self.products = []

    def insert_product(self, product):
        self.products.append(product)

    def show_product(self):
        for product in self.products:
            print(product.name, product.value)

    def total_sum(self):
        total = reduce(lambda total, product: total + product.value, self.products, 0)
        return total


class Product:
    def __init__(self, name, value):
        self.name = name
        self.value = value
