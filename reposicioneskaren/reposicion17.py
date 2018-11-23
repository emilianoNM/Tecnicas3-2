def potencia(b,e):
pila=[]
while e>0:
	if e%2==0:
		pila.append(True)
		e /=2
	else:
		pila.apped(False)
		e=(e-1)/2
pot=1
while pila:
	es_par=pila.pop()
	if es_par:
		pot=pot*pot
	else:
		pot=pot*pot*b
return pot
