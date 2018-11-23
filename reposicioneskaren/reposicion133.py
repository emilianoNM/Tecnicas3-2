def producto(a,b):
	if(a<b):
		return producto(b,a)
	elif(b!=0):
		return (a+producto(a,b-1))
	else:
		return 0
a=int(input("escribe el primer numero:"))
b=int(input("escribe el segundo numero:"))
print("producto es", producto(a,b))
