#encoding: latin1
#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
hab_A = 80000
hab_B = 200000
tax_A = 3.0
tax_B = 1.5

anos = 0
while hab_A < hab_B:
  anos  += 1
  hab_A += round((hab_A*tax_A/100))
  hab_B += round((hab_B*tax_B/100))

print('Em '+ str(anos) + ' anos a população do país A será maior que a população do país B')
print('Habitantes país A = ' + str(hab_A) )
print('Habitantes país B = ' + str(hab_B) ) 
