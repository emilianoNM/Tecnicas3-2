import random
a=[]
n=int(input("Escribe numero de elementos:"))
for j in range(n):
	a.append(random.randint(1,20))
print("lista:",a)
