import math
import sys

def eea(a,b):
	an = a
	bn = b
	xn = y = 1
	x = yn = 0
	r = a%b
	while (an%bn) != 0:
		r = gcd = an%bn
		an = bn
		bn = r
		c = -(a/b)
		temp = x
		x = (x*a)+xn	
		xn = temp
		y = (math.ceil(abs(float(a*x)/float(b))))*(x/abs(x))
	print gcd
	return gcd

eea(7049, 1802)