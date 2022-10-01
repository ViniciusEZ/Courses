from day5 import data
from data import products, people, list1

from functools import reduce

media = reduce(lambda ac, p: ac + p['age'], people, 0) / len(people)
print(media)

