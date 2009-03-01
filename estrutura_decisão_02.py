#encoding: latin1 
numero = float(raw_input('Insira um número '))
if numero == 0:
	print('Zero é o único número que não é nem positivo, nem negativo.')
elif numero > 0:
		print('O número '+ str(numero) +' é positivo.')
else:
		print('O número '+ str(numero) +' é negativo.')

