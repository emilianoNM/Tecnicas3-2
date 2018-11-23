import math
n=int(input("escribe numero de terminos:"))
sum1=1
for i in range(1,n+1):
	sum1=sum1+(1/math.factorial(i))
print("La suma de las series es,"round(sum1,2))
