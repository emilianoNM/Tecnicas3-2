import arbol

nodo1=arbol.nodo('rais',None)
nodo2=arbol.nodo('n1',nodo1)
nodo3=arbol.nodo('n2',nodo1)
nodo4=arbol.nodo('n3',nodo2)
a=arbol.nodo('A',None)
#print (arbolbinario(a))
miprimerarbol=arbol.arbolbinario(a)
miprimerarbol.addnodo(arbol.nodo('B',None))
miprimerarbol.addnodo(arbol.nodo('C',None))
miprimerarbol.addnodo(arbol.nodo('D',None))
miprimerarbol.addnodo(arbol.nodo('E',None))
miprimerarbol.addnodo(arbol.nodo('F',None))
miprimerarbol.addnodo(arbol.nodo('G',None))
miprimerarbol.addnodo(arbol.nodo('H',None))
miprimerarbol.addnodo(arbol.nodo('I',None))

miprimerarbol.addnodo(arbol.nodo('J',None))
miprimerarbol.addnodo(arbol.nodo('K',None))
miprimerarbol.addnodo(arbol.nodo('L',None))
miprimerarbol.addnodo(arbol.nodo('M',None))
miprimerarbol.addnodo(arbol.nodo('N',None))
miprimerarbol.addnodo(arbol.nodo('O',None))


print a 
for hijo in a.gethijos():
	print "  ",hijo

	for hijo2 in hijo.gethijos():
		print "       ",hijo2
		for hijo3 in hijo.gethijos():
			print " 		",hijo3
			for hijo4 in hijo.gethijos():
				print "					",hijo4
				

#print (nodo1.esraiz())
#print (nodo2.esraiz())
#print (nodo3.esraiz())
print a.gethijos()
