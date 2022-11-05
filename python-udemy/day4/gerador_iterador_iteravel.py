import sys
import time

# lista = [0,1,2,3,4,5]
# lista = iter(lista)
#
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
#
# print(hasattr(lista, '__next__'))

# def gera():
#     r = []
#     for n in range(100):
#         yield n
#         time.sleep(0.1)
#
# g = gera()
# for v in g:
#     print(v)

lista = (x for x in range(1000))
print(type(lista))

