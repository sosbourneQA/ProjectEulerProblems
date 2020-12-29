# 4. Largest Palindrome Product

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def compute():
    print(str(103 * 607))
    #  [::-1] in line 11 follows the pattern of 'start : stop : steps' WHERE
    #  start = the beginning index of the slice (defaults to index 0)
    #  stop = where the slice ends (defaults to index -1)
    #  steps = the interval at which it counts (negative values result in it counting backwards)

    print(str(103 * 607)[::-1])

    ans = max(i * j
              for i in range(100, 1000)
              for j in range(100, 1000)
              if str(i * j) == str(i * j)[:: -1])
    return str(ans)



print(compute())
