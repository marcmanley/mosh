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
