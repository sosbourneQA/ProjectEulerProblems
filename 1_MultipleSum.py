# 1. Multiples of 3 and 5

# If we list all the natural numbers below 10 that are
# multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.



# SOLUTION FROM 'PROJECT NAYUKI'

# def compute():
# 	ans = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
# 	return str(ans)
#
#
# if __name__ == "__main__":
# 	print(compute())





def muiltipleSum():

    total = 0
    x = 0

    while x < 1000:
        if x % 5 == 0 or x % 3 == 0:
            total += x
        x += 1
    return total

    print(total)

print(muiltipleSum())
