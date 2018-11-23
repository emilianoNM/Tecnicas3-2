lista=[4,2,7,8,4,8,2,5,1,9,10]
lista.sort()
rep=[]
n=len(lista)
print lista
for i in range (1,n-1):
	if lista[i]==lista[i+1]:
		print('///Repetido: ',lista[i])
		rep.append(i)
		
		

j=0
for i in rep:

	lista.pop(i-j)
	j+=1

print lista