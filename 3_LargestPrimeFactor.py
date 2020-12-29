# 3. Largest Prime Factor

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

plist = [2]


def factors(number):
	for prime in primes(2, number):
		if number % prime == 0:
			# number /= prime
			number = number / prime
			yield prime
		elif number == 1:
			break


def primes(min, max):
	# if 2 >= min: yield 2
	for i in range(3, max, 2):
		for p in plist:
			if i % p == 0 or p * p > i:
				break
			elif i % p:
				plist.append(i)
				if i >= min: yield i


print(max(factors(600851475143)))









