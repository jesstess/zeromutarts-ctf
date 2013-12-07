#!/usr/bin/env python

import sys

n= 80646413
e = 5

# You'll have to find the d yourself..
d = unknown

f = open( sys.argv[1] , "r" )
for line in f: 
    line = int(line.strip())
    # you'll have to insert the decrypt function for each line(number) here!
    #dec = ...
    print chr(dec)




# might come handy
def xgcd(a,b):
    """Extended GCD:
    Returns (gcd, x, y) where gcd is the greatest common divisor of a and b
    with the sign of b if b is nonzero, and with the sign of a if b is 0.
    The numbers x,y are such that gcd = ax+by."""
    prevx, x = 1, 0;  prevy, y = 0, 1
    while b:
        q, r = divmod(a,b)
        x, prevx = prevx - q*x, x
        y, prevy = prevy - q*y, y
        a, b = b, r
    return a, prevx, prevy

def modinv(a, m):
    """Modular multiplicative inverse, i.e. a^-1 = 1 (mod m)"""
    a, u, v = xgcd(a, m)
    if a <> 1:
        raise Exception('No inverse: %d (mod %d)' % (a, m))
    return u

