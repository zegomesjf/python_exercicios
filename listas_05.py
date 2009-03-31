#!/usr/bin/python2.5
# Faca um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
# cujos valores deverao ser compostos pelos elementos intercalados dos dois outros vetores

import string
from itertools import imap

class Intersperse(object):
	def __init__(self):
		self.vector_1 = [0,1,2,3,4,5,6,7,8,9]
		self.vector_2 = [9,8,7,6,5,4,3,2,1,0]
		self.vector_3 = []
		self.intersperse()

	def intersperse(self):
		length = len(self.vector_1)
		for i in xrange(length):
			self.vector_3.append(self.vector_1[i])
			self.vector_3.append(self.vector_2[i])

	def __str__(self):
		return string.join(imap(str, self.vector_3), ', ')	

# run --------
i = Intersperse()
print i