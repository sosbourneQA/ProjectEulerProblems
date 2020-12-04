# If we list all the natural numbers below 10 that are
# multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def muiltipleThree():

    three_total = 0
    n = 0

    while 3 * n < 1000:
        n += 1
        num = 3 * n
        three_total += num
    return three_total

    print(three_total)




def muiltipleFive():

    five_total = 0
    x = 0

    while 5 * x < 1000:
        x += 1
        num = 5 * x
        five_total += num
    return five_total

    print(five_total)


print(muiltipleFive())
print(muiltipleThree())

print(muiltipleFive() + muiltipleThree())


def compute():
	ans = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
	return str(ans)


if __name__ == "__main__":
	print(compute())