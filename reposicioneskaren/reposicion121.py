a=[]
n=int(input("escribe total de elementos/"))
for i in range(1,n+1):
	a1=int(input("escribe elemento"))
	a.append(a1)
for i in range(0,len(a)):
	for j in range(0,len(a)-i-1):
		if(a[j]>a[j+1]):
			t=a[j]
			a[j]=a[j+1]
			a[j+1]=t
print("El numero mas grande es:",a[n-2])

