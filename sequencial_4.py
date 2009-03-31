nota=[]
for i in range(4):
  nota.append(float(raw_input("informe a nota do bimestre "+str(int(i)+1)+" :")))
print "A media eh: ", str(sum(nota) / len(nota))
