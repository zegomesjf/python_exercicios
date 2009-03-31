#encoding: latin1
# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

def retorna_nome_senha():
  nome = raw_input('Digite seu nome: ')
  senha = raw_input('Digite sua senha: ')
  return nome, senha

nome, senha = retorna_nome_senha()

while nome == senha:
  print('Erro: Nome e senha não podem ser iguais')
  nome, senha = retorna_nome_senha()
