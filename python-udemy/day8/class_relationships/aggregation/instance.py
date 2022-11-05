from day8.class_relationships.aggregation.aggregation import *

cart = Shoppingcart()
p1 = Product('Shirt', 10)
p2 = Product('Samsung', 1000)
p3 = Product('Cup', 20)

cart.insert_product(p1)
cart.insert_product(p2)
cart.insert_product(p3)
cart.insert_product(p2)

cart.show_product()
print(cart.total_sum())
