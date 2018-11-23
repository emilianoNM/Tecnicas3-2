import math
print("Escribe los coeficientes de un polinomio de tercer grado")
lst=[]
for i in range(0,4):
	a=int(input("Escribe coeficiente:"))
	lst.append(a)
x=int(input("Escribe valor de x:"))
sum1=0
l=3
for i in range(0,3):
	while(l>0):
		sum1=sum1+(lst[i]*math.pow(x,l))
		break
	l=l-1
sum1=sum1=lst[3]
print("El valor del polinomio es:",sum1)
