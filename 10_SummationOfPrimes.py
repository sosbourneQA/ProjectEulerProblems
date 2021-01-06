# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

import math

def isPrime(num):
    # Iterates from 2 to sqrt(num)+1 as discussed above
    # Make sure to convert sqrt to int for range
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i == 0):
            return False
    return num

def calculate():

    total = 0

    for i in range(2, 2000000):
        if isPrime(i):
            total += i
            print(total)
    return total


print(calculate())