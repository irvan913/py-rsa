import math, random, sys


def eea(a,b):
	an = max(a,b)
	bn = min(a,b)
	xn = y = 1
	x = 0
	r = 0
	while (an%bn) != 0:
		c = -(an/bn)
		r = an%bn
		an = bn
		bn = r
		temp = x
		x = (x*c)+xn
		xn = temp
		try:
			y = (round(abs(float(max(a,b)*x)/float(min(a,b)))))*(x/abs(x))*(-1)
		except BaseException:
			y = 0
	result = (r, x, y)
	return result


def gcd(a,b):
	an = max(a,b)
	bn = min(a,b)
	while (an%bn) != 0:
		r = an%bn
		an = bn
		bn = r
	return r


def miller_rabin_check(a,s,d,n):
	c1 = pow(a,d,n)
	if c1 == 1:
		return True
	for i in xrange(1, s-1):
		if c1 == n-1:
			return True
		c1 = (c1*c1)%n
	return c1 == n-1


def miller_rabin(n):
	d = n-1
	s = 0
	while d % 2 == 0:
		d = d/2
		s += 1
	for i in range(20):
		a = random.randrange(1, n)
		if not miller_rabin_check(a,s,d,n):
			return False
	return True


def gen_prime(bits):
	b = int(bits)
	while True:
		n = random.getrandbits(b)
		n |=2**b| 1
		if miller_rabin(n):
			return n
			break


def rsa_keygen():
	p = gen_prime(256)
	q = gen_prime(256)
	n = p*q
	phi_n = (p-1)*(q-1)
	while True:
		e = random.randrange(1, phi_n)
		if gcd(phi_n, e) == 1:
			break
	d = eea(e,phi_n)[1]
	public = (e,n)
	private = (d,n)
	return (public, private)


def rsa_encrypt(M,e,n):
	M = ''.join(str(ord(i)) for i in M)
	if M < n:
		return pow(M,e,n)
	else:
		return 'message is too long'


def rsa_decrypt(C,d,n):
	return pow(C,d,n)


