from itertools import permutations
import itertools

listA = [21, 18, 19]
permutations = itertools.permutations(listA)

for i in list(permutations):
    print(i)
