# Part I ­ Implement the Fibonnaci Sequence
def fib(n) :
	if n == 1 or n == 2 :
		return 1
	return fib(n -1) + fib(n -2)

# Part II ­ Implement Euclid’s GCD Algorithm
def gcd2(a, b):
	if a == 0:
		return b
	elif b == 0:
		return a
    
	return gcd2(b, a % b)

# Part III ­ String Comparison
def compareTo(s1, s2):
	if not s1 == '' and not s2 == '':
		if s1[0] < s2[0]:
			return -1
		if s1[0] == s2[0]:
			return 0
		return 1, compareTo(s1[1:], s2[1:])
