#encoding: latin1 
#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
notas = [0] * 4
for x in range(4):
  notas[x] = float(raw_input('Digite a nota do ' + str(x+1) + ' bimestre: '))
print('A média é: ' + str( sum(notas) / len(notas)))
