#--encoding: latin1--
#1 litro para cada 3 metros
#1 lata tem 18l e custa 60 reias
metros_quadrados = float(raw_input("informe a quantidade de metros: "))
qtd_latas = ((metros_quadrados / 3) // 18)
if (((metros_quadrados / 3) % 18) > 0):
  qtd_latas = qtd_latas + 1
print U"custará: ", qtd_latas * 60, " reais."
