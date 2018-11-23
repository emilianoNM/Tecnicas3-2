a=[]
n=int(input("escribe numero de elementos en lista"))
for x in range(0,n):
	elemento=int(input("escribe elemento"+str(x+1)+":"))
	a.append(elemento)
t=a[0]
a[0]=a[n-1]
a[n-1]=t
print("nueva lista")
print(a)
