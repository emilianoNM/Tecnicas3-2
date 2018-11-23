n=int(input("Escribe numero de terminos:"))
sum1=0
for i in range(1,n+1):
	sum1=sum1+(1/i)
print("la suma de las serie es:",round(sum1,2))
