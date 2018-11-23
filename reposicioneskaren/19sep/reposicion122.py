a=[]
n=int(input("escribe numero de elementos:))
for i in range(1,n+1):
	x=input("escribe elemento")
	a.append(x)
a.sort(key=len)
print(a)

