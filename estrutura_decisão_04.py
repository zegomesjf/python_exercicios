ano = float(raw_input('Insira um ano no formato AAAA. ex. 1983\n'))
if ano%400 == 0:
  print('E ano bissexto.')
elif ano%100 == 0:
  print('Nao e ano bissexto.')
elif ano%4 == 0:
	print('E ano bissexto')
else:
  print('Nao e ano bissexto.')
