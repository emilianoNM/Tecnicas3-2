#testArbol.py
import Arbol

nodo1=Arbol.Nodo('Raiz',None)
nodo2=Arbol.Nodo('N1',nodo1)
nodo3=Arbol.Nodo('N2',nodo1)
nodo4=Arbol.Nodo('N3',nodo2)
print (nodo1.esRaiz())
print (nodo2.esRaiz())
print (nodo3.esRaiz())	
print (nodo1)

print (nodo1.getHijos())
print (nodo1.esHoja())
print (nodo2.esHoja())
print (nodo3.esHoja())
print (nodo4.esHoja())

nodo2.delete()

print (nodo1.esRaiz())
print (nodo2.esRaiz())
print (nodo1.getHijos())
