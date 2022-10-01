# lista = [
#     ('chave', 2),
#     ('chave2', 5)
# ]

# d1 = {x:y*10 for x, y in lista}
d1 = {f'chave {x}': x**2 for x in range(5)}
print(d1)