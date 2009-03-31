#!/usr/bin/python2.5
# Faca um Programa que leia 20 numeros inteiros e armazene-os num vetor. 
# Armazene os numeros pares no vetor PAR e os 
# numeros IMPARES no vetor impar. Imprima os tres vetores.

import string
from itertools import imap

class ParImpar(object):
	def __init__(self):
		self.v   	 = []
		self.par 	 = []
		self.impar = []
		self.vector()
		self.separar()

	def vector(self):
		for i in range(0,20):
			self.v.append(i)
			
	def separar(self):
			for i in self.v:
				if (i%2 == 0): self.par.append(i)
				else: self.impar.append(i)
			
	def __str__(self):
		vector = string.join(imap(str, self.v), ', ')
		par    = string.join(imap(str, self.par), ', ')
		impar  = string.join(imap(str, self.impar), ', ')
		return 'vetor: %s\npares: %s\nimpares: %s' % (vector, par, impar)

# run --------
p = ParImpar()
print p