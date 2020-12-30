# The sum of the squares of the first ten natural numbers is,
#
# The square of the sum of the first ten natural numbers is,
#
# Hence the difference between the sum of the squares of the
# first ten natural numbers and the square of the sum is .
#
# Find the difference between the sum of the squares of the
# first one hundred natural numbers and the square of the sum.

def calculator():

    total = 0
    sq = 0

    for x in range(1, 101):
        num = x * x
        total += num
        sq += x
        print(sq)
    return ((sq * sq) - total)


print(calculator())
