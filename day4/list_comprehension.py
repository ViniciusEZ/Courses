l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l3 = [var for var in l1]
l2 = [var * 2 for var in l1]
# print(l2)
# l4 = [(v,v2) for v in l1 for v2 in range(3)]
# print(l4)
l5 = ['Luiz', 'Mauro', 'Maria']
ex6 = [name.replace('a', '@') for name in l5]

tup = (
    ('chave', 'valor'),
    ('chave2', 'valor2')

)
# ex7 = [(x,y) for x, y in tup]
# ex7 = dict(ex7)
# print(ex7)

list8 = list(range(100))
ex8 = [n for n in list8 if n % 2 == 0 if n % 8 == 0]


ex9 = [v if v % 3 == 0 else 0 for v in list8]
print(ex9)