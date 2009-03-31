#encoding: latin1 
vogais = ['a', 'e', 'i', 'o', 'u']
letra = raw_input('Digite uma letra: ')
print('e uma vogal') if vogais.count(letra) != 0 else ('nao e uma vogal')
