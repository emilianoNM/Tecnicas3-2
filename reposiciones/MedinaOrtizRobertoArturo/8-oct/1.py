lista=[1,2,3,5,7,6,8,9,10]
n=len(lista)+1
esp=n*(n+1)/2
sum=0
for i in lista:
	sum=sum+i

print ('El faltante es: ',esp-sum)