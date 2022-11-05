# '''
# Zip - Unindo iteráveis
# Zip_longest - Itertools
# '''
from itertools import zip_longest, count


# Code
index = count()
cities = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
states =  ['SP', 'MG', 'BA']
cities_states = zip(
    index,
    states,
    cities
)
#
for index, state, city in cities_states:
    print(index, state, city)
