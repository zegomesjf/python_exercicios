#!/usr/bin/python2.5
# Em uma competicao de salto em distancia cada atleta tem direito a cinco saltos. O resultado do 
# atleta sera determinado pela media dos cinco valores restantes. Voce deve fazer um programa que 
# receba o nome e as cinco distancias alcancadas pelo atleta em seus saltos e depois informe o nome, 
# os saltos e a media dos saltos. O programa deve ser encerrado quando nao for informado o nome do 
# atleta.

import string

class Salto(object):
	def __init__(self):
		self.v = []
		self.vector()
		self.result()
	
	def vector(self):
		while 1:
			name = raw_input('Nome do atleta')
			if name == '\n' or name == '': 
				break
			else: self.gets(name)

	def gets(self, name):
		distances = []
		for i in range(1,6):
			d = raw_input('%d Salto' % i )
			distances.append(d)
		self.__push__(name, distances)

	def result(self):
		for v in self.v:
			print '\n\n\nAtleta: %s\n' % v['name']
			
			print 'Primeiro Salto: %s m' % v['distances'][0]
			print 'Segundo Salto:  %s m' % v['distances'][1]
			print 'Terceiro Salto: %s m' % v['distances'][2]
			print 'Quarto Salto:   %s m' % v['distances'][3]
			print 'Quinto Salto:   %s m' % v['distances'][4]
			
			print '\n\nResultado Final:'
			print 'Atleta: %s' % v['name']
			print 'Saltos: %s' % string.join(v['distances'], ' - ') 
			print 'Media dos saltos: %0.1f m' % (sum(map(float, v['distances'])) / 5)
	
	def __push__(self, name, distances):
		a = { 'name': name, 'distances': distances }
		self.v.append(a)

s = Salto()