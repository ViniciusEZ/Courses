import re


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount(self, percentage):
        self.price = self.price - (self.price * (percentage / 100))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.upper()

    # Getter
    @property
    def price(self):
        return self._price

    # Setter
    @price.setter
    def price(self, value):
        if isinstance(value, str):
            value = re.sub(r'[a-zA-Z]*([^0-9,]+)', '', value).replace(',', '.')
        self._price = float(value)


p1 = Product('Shirt', 50)
p1.discount(10)
print(p1.name, p1.price)

p2 = Product('Cup', '30,30')
p2.discount(10)
print(p2.name, p2.price)
