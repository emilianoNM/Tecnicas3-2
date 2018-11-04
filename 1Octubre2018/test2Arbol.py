#test2Arbol.py
import Arbol

A=Arbol.Nodo('A',None)


MiPrimerArbol=Arbol.ArbolBinario(A)
#MiPrimerArbol=Arbol.ArbolBinario(B)
MiPrimerArbol.addNodo(Arbol.Nodo('B',None))
MiPrimerArbol.addNodo(Arbol.Nodo('C',None))
MiPrimerArbol.addNodo(Arbol.Nodo('F',None))
MiPrimerArbol.addNodo(Arbol.Nodo('G',None))
MiPrimerArbol.addNodo(Arbol.Nodo('J',None))
MiPrimerArbol.addNodo(Arbol.Nodo('K',None))
MiPrimerArbol.addNodo(Arbol.Nodo('L',None))
MiPrimerArbol.addNodo(Arbol.Nodo('M',None))
MiPrimerArbol.addNodo(Arbol.Nodo('LL',None))
MiPrimerArbol.addNodo(Arbol.Nodo('N',None))
MiPrimerArbol.addNodo(Arbol.Nodo('O',None))
for x in xrange(1,23):
	MiPrimerArbol.addNodo(Arbol.Nodo(x,None))

print MiPrimerArbol
