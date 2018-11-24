lista=[3,1,6,4,1,7,9,3,6,10]
n=len(lista)
max=min=lista[1]
for i in range(1,n):
	if lista[i]<min:
		min=lista[i]
	if lista[i]>max:
		max=lista[i]

print ('Minimo: ',min,' maximo: ',max)