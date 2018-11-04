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
print (A)
for  hijo in  A.getHijos():
	print ("   ",hijo)
	for hio2hijo in hijo.getHijos():
		print ("        ",hio2hijo)
		for hio2hijo2hijo in hio2hijo.getHijos():
			print ("           ",hio2hijo2hijo)