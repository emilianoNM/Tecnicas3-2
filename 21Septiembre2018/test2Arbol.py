#test2Arbol.py
import Arbol

A=Arbol.Nodo('A',None)
B=Arbol.Nodo('B',A)
C=Arbol.Nodo('C',A)
D=Arbol.Nodo('D',B)
E=Arbol.Nodo('E',B)
F=Arbol.Nodo('F',C)
G=Arbol.Nodo('G',C)
H=Arbol.Nodo('H',D)
I=Arbol.Nodo('C',D)
J=Arbol.Nodo('J',E)
K=Arbol.Nodo('K',E)
print A
for nodo in A.getHijos():
	print ' ',nodo
	for nodoN2 in nodo.getHijos():
		print '    ',nodoN2
		for nodoN3 in nodoN2.getHijos():
			print '        ',nodoN3
