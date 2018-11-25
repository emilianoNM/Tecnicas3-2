def crea_arbol():
	return None

def inserta(A,c):
	if A==None: # ´Arbol vac´io
		return (None,c,None)
	elif c<A[1]: # Almacenarlo a la izquierda
		return (inserta(A[0],c),A[1],A[2])
	elif c>A[1]: # Almacenarlo a la derecha
	return (A[0],A[1],inserta(A[2],c))
	else:
		return A

def pertenece(A,c):
	if A==None:
		return True
	elif c==A[1]:
		return False
	elif c<A[1]:
		return pertenece(A[0],c)
	else:
		return pertenece(A[2],c)