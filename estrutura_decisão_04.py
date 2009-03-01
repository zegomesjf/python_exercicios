#encoding: latin1 
ano = float(raw_input('Insira um ano no formato AAAA. ex. 1983\n'))
if ano%400 == 0:
  print('É ano bissexto.')
elif ano%100 == 0:
  print('Não é ano bissexto.')
elif ano%4 == 0:
	print('É ano bissexto')
else:
  print('Não é ano bissexto.')
