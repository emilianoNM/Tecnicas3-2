lista=['a','b','c','d','h','e','u','w','i','c','q','u','b','h']
lista.sort()
print lista
n=len(lista)
for i in range (1,n-1):
	if lista[i]==lista[i+1]:
		print('///Repetido: ',lista[i])
		