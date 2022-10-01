'''
count - Itertools
'''

from itertools import count

contador = count(start=5, step=-1)
list1 = ['Vinicius', 'Beato', 'Carlos', 'Magno']
list1 = zip(count(), list1)
print(list(list1))
for value in contador:
    print(value)
    if value == -5:
        break