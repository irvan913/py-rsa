import math

def primes(mn, mx):
	# """
	# AKS primality test 
	# """
	# def AKS(n):
	# 	
	"""
	sieve of eratosthenes
	"""
	for i in range(mn, mx):
		print 'x'

def gcd(a,b):
	an = max(a,b)
	bn = min(a,b)
	while (an%bn) != 0:
		r = an%bn
		an = bn
		bn = r
	return r

gcd(3454252452343242342341234, 423241234334342)