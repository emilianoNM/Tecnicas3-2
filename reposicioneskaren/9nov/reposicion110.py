lista=[1,2,3,['a','b','c','d'],4,5]
def listar(lista):
	for n in lista:
		if isinstance(n,lista):
			listar(n)
		else:
			print n
