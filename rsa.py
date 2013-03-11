import math, pdb
import sys

def eea(a,b):
	an = max(a,b)
	bn = min(a,b)
	xn = y = 1
	x = 0
	while (an%bn) != 0:
		c = -(an/bn)
		r = an%bn
		an = bn
		bn = r
		temp = x
		x = (x*c)+xn
		xn = temp
		y = (round(abs(float(max(a,b)*x)/float(min(a,b)))))*(x/abs(x))*(-1)
	result = (r, x, y)
	return result