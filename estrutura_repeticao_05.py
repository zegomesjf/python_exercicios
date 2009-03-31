#encoding: latin1
#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
#Valide a entrada e permita repetir a operação.

hab_A = 0
hab_B = 0
tax_A = 0
tax_B = 0

while hab_A < 1:
  hab_A = int(raw_input('Informe a população do país A '))

while hab_B < 1:
  hab_B = int(raw_input('Informe a população do país B '))

while tax_A <= 0:
  tax_A = float(raw_input('Informe a taxa de crescimento da população do país A '))

while tax_B <= 0:
  tax_B = float(raw_input('Informe a taxa de crescimento da população do país B '))

anos = 0
while hab_A < hab_B:
  anos  += 1
  hab_A += round((hab_A*tax_A/100))
  hab_B += round((hab_B*tax_B/100))

print('Em '+ str(anos) + ' anos a população do país A será maior que a população do país B')
print('Habitantes país A = ' + str(hab_A) )
print('Habitantes país B = ' + str(hab_B) )
