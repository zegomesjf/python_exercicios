notas = [0] * 4
for x in range(4):
  notas[x] = float(raw_input('Digite a nota do ' + str(x+1) + ' bimestre: '))

print('A media eh: ' + str( sum(notas) / len(notas)))
