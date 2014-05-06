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
			y = int((round(abs(float(max(a,b)*x)/float(min(a,b)))))*(x/abs(x))*(-1))
		except BaseException:
			y = 0
	result = (r, x, y)
	print result
	return result

# eea(17,2668)

def gcd(a,b):
	an = max(a,b)
	bn = min(a,b)
	r = 0
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
	p = gen_prime(16)
	q = gen_prime(16)
	n = p*q
	phi_n = (p-1)*(q-1)
	while True:
		e = random.randrange(1, phi_n)
		if gcd(phi_n, e) == 1:
			break
	result = eea(e,phi_n)
	d = result[2]
	while d < 0:
		d += phi_n
	public = (e,n)
	private = (d,n)
	return (public, private)


def rsa_encrypt(M,e,n):
	# M = ''.join(str(ord(i)) for i in M)
	return pow(int(M),e,n)


def rsa_decrypt(C,d,n):
	c = pow(C,d,n)
	# M = ''.join(str(chr(i)) for i in int(c))
	return C


def encrypt(M):
	key = rsa_keygen()
	e = key[0][0]
	n = key[0][1]
	d = key[1][0]
	C = rsa_encrypt(M,d,n)
	result = rsa_decrypt(C,e,n)
	print "this is the cypertext:"
	print C
	print "and this is the plaintext:"
	print result