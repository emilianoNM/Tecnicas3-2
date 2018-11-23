def llenar(n):
	for i in range(0,n+1):
		r.append(0)
	return r


def sumar(a,b,r,n):
	for i in range(n,0,-1):
		r[i]=r[i]+a[i-1]+b[i-1]

		if r[i]>=10:
			r[i]=r[i]-10
			r[i-1]=1
		

	print r





a=[5,6,3]
b=[8,4,2]
n=len(a)
m=len(b)
r=[]
if n>m:
	r=llenar(n)
	sumar(a,b,r,n)


elif n<m:
	r=llenar(m)
	sumar(a,b,r,m)

else: 
	r=llenar(n)
	sumar(a,b,r,n)