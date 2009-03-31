#!/usr/bin/python2.5
# Faca um Programa que leia um vetor de 10 numeros reais e mostre-os na ordem inversa.

import string
from itertools import imap

class Reverse(object):
	def __init__(self):
		self.v = []
		self.vector()
	
	def vector(self):
		for i in range(0,10):
			self.v.append(i)
		self.v = sorted(self.v, reverse = True)
	
	def __str__(self):
		return string.join(imap(str, self.v), ', ')


# run --------
r = Reverse()
print r