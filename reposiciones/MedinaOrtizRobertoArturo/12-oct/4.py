lista=[2,6,7,3,8,9,2,5,8,1,10,4]
n=len(lista)
valor=10
for i in range(1,n-1):
	pivote=lista[i]
	for j in range (i,n):
		if pivote+lista[j]==valor:
			print ('Pareja de valores ',pivote,lista[j])