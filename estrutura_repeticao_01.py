#encoding: latin1
#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
nota = int(raw_input('Digite uma nota entre zero e dez. \n'))
while nota < 0 or nota > 10:
  print('Nota inválida.\n')
  nota = int(raw_input('Digite uma nota entre zero e dez.\n'))
