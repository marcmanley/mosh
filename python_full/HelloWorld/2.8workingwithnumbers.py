from math import factorial
from collections import Counter
import operator
from itertools import permutations
import math

print(round(2.9))
print(abs(-2.9))  # absolute vaue

print(math.ceil(2.2))  # the ceiling of a number
print(math.floor(9.8))

print(sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))
print(math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))

print(math.gcd(42, 7))

# Python code to demonstrate gcd()
# method exceptions

# prints 0
print("The gcd of 50 and 8 is: ", end="")
print(math.gcd(50, 8))

# Produces error
# print("\nThe gcd of a and 13 is: ", end="")
# print(math.gcd('a', 13))

# A Python program to print all
# permutations using library function

print("Permutations of (1, 2, 3, 4, 5)")

# Get all permutations of [1, 2, 3]
perm = permutations([1, 2, 3, 4, 5])

# Print the obtained permutations
for i in list(perm):
    print(i)


def perm(i):
    num = factorial(len(i))
    mults = Counter(i).values()
    den = reduce(operator.mul, (factorial(v) for v in mults), 1)
    return num / den
