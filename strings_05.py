#encoding: latin1 
#Nome na vertical

name = raw_input('Digite seu nome: ')
sub_name = ''
for i in range(len(name)):
    print name[:len(name)-i:]

