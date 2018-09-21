#Arbol.py
class Nodo(object):
	"""docstring for Nodo"""
	def __init__(self, id,padre):
		super(Nodo, self).__init__()
		self.id = id
		self.padre=padre
		self.hijos=[]
		if padre!=None:
			padre.addHijo(self)

	def addHijo(self,hijo):
		self.hijos.append(hijo)
	def esHoja(self):
		return len(self.hijos)==0
	def delete(self):
		if(self.esRaiz()):
		   pass
		else:
		   padre=self.padre
		   hijos=padre.getHijos()
		   hijos.remove(self)
		   self.padre=None

	def esRaiz(self):
		return self.padre==None
	def getHijos(self):
		return self.hijos
	def __str__(self):
		return self.id 
	def __repr__(self):
		return self.id



class Arista(object):
	"""docstring for Arista"""
	def __init__(self, arg):
		super(Arista, self).__init__()
		self.arg = arg

class ArbolBinario(object):
	"""docstring for Arbol"""
	#balanceado 
	#Recorrido en profundidad-primero
    #Recorrido en anchura-primero
	def __init__(self, arg):
		super(Arbol, self).__init__()
		self.arg = arg
	def addNodo(self):
			pass
	def __str__(self):
			pass	
		