#encoding: latin1
#Faça um programa que leia e valide as seguintes informações:
#				   a. Nome: maior que 3 caracteres;
#					    b. Idade: entre 0 e 150;
#							   c. Salário: maior que zero;
#								    d. Sexo: 'f' ou 'm';
#										   e. Estado Civil: 's', 'c', 'v', 'd';


nome = ''
idade = 0
salario = 0
sexo = ''
estado_civil = ''

while len(nome)<=3:
  nome = raw_input('Nome: (com mais de 3 letras)')

while idade < 0 or idade > 150 :
  idade = raw_input('Idade:(entre 0 e 150) ')

while salario <= 0:
  salario = raw_input('Salário: (maior que 0) ')

while sexo <> 'f'  and sexo <> 'm':
  sexo = raw_input('Sexo: [m/f]')

while estado_civil <> 's' and estado_civil <> 'c' and estado_civil <> 'v' and estado_civil <> 'd':
  estado_civil = raw_input('Estado Civil: [s/c/v/d]')
