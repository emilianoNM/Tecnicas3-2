def printnumero(upper):
	if(upper>0):
		printnumero(upper-1)
		print(upper)
upper=int(input("Escribe limite superio:"))
printnumero(upper)