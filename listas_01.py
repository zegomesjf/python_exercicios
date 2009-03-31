#!/usr/bin/python2.5
# Utilizando listas faca um programa que faca 5 perguntas para uma pessoa sobre um crime.

class Criminal(object):
	def __init__(self):
		self.yes = 0
		self.no  = 0
		self.asks()
		
	def asks(self):
		questions = ['Telefonou para a vitima?', 
								 'Esteve no local do crime?', 
								 'Mora perto da vitima?',
								 'Devia para a vitima?',
								 'Ja trabalhou com a vitima?'
								]
		for i in questions:
			self.gets(i)

	def answer(self, answer):
		if answer == 's': self.yes += 1

	def gets(self, ask):
		while 1:
			a = raw_input(ask)
			if a == 's' or a == 'n' : break
		self.answer(a)

	def __str__(self):
		if 		self.yes == 2: return 'Suspeito'
		elif 	self.yes == 3 or self.yes == 4: 
			return 'Cumplice'
		elif 	self.yes == 5: return 'Assassino'
		else: 							 return 'Inocente'


# run --------
c = Criminal()
print "\n\n\n\nSeu indiciado e: %s" % c