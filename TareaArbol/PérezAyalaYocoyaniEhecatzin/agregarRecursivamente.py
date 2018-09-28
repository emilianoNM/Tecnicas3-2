import Arbol 

def agregarRecursivamente(nodos, arbol):
	
	if len(nodos) > 0:
		arbol.addNodo(nodos[0], None, True)
		nodos.remove(nodos[0])
		agregarRecursivamente(nodos, arbol)


def imprimirArbol(hijos, cont):
	for hijo in hijos:
		if hijo.esHoja() == False:
			print('   '*cont, hijo)
			imprimirArbol(hijo.getHijos(), cont+1)
		else :
			print('   '*cont, hijo)
	
def main():
	A=Arbol.Nodo('A',None)
	numeroDeNodos = 14
	nodos = []

	for creacion in range(numeroDeNodos):
		nodos.append(Arbol.Nodo(chr(ord('B')+creacion),None))

	miArbol = Arbol.ArbolBinario(A)
	agregarRecursivamente(nodos, miArbol)
	print('A')
	imprimirArbol(A.getHijos(), 1)

main()