lista=[1,2,3,4,5,6,7,8,9,10]
lista2=[]
n=len(lista)-1
for i in range(n,-1,-1):
	lista2.append(lista[i])

print ('Original: ',lista)
print ('Inverso: ',lista2)