lista=[4,2,7,8,4,8,2,5,1,9,10]
lista.sort()
n=len(lista)
for i in range (1,n-1):
	if lista[i]==lista[i+1]:
print('///Repetido: ',lista[i])