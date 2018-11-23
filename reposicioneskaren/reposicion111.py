numero=int(input("introduce numero:"))
if numero>1:
	for in in range(2,numero):
		if(numero%i)==0:
			print(numero,"no es numero primo")
			print(i,"veces",numero//i,"es",numero)
		break
		else:
			print(numero,"es numero primo")
		else:
			print(numero,"no es numero primo")
