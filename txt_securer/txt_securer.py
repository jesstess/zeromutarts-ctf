#!/usr/bin/env python
import base64
import os
def xor(data, key):
	return "".join(map(lambda (x,y): chr(ord(x) ^ ord(y)), zip(data, key*(len(data)/len(key)+1))))

keylen = 16

def generate_key():
	return os.urandom(keylen)

def encrypt(data, key):
	return base64.b64encode(xor(data, key))

def decrypt(data, key):
	return xor(base64.b64decode(data), key)
