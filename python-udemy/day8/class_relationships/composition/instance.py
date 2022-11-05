from day8.class_relationships.composition.composition import *


client1 = Client('Vinicius', 19)
client1.insert_address('São Paulo', 'SP')
print(client1.name)
client1.show_addresses()
print()
client2 = Client('Mary', 29)
client2.insert_address('Rio de Janeiro', 'RJ')
client2.insert_address('Bahia', 'BH')
print(client2.name)
client2.show_addresses()
print()
client3 = Client('Jonatas', 20)
client3.insert_address('Santa Catarina', 'SC')
print(client3.name)
client3.show_addresses()
