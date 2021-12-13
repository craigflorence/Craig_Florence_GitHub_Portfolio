# Ask the user for a number and determine whether the number is prime or not.

import math

a = 2

if sum([True if a % factor == 0 else False for factor in ([2] + list(range(3, int(math.sqrt(a)) + 1, 2)))]):
    print("Number is composite")
else:
    print("Number is prime")


