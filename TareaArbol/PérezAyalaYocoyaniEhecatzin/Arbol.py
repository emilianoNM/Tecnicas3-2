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
		hijo.padre=self
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

class ArbolBinario(object):
	"""docstring for ArbolBinario"""
	#balanceado 
	#Recorrido en profundidad-primero
    #Recorrido en anchura-primero
	def __init__(self, nodo):
		super(ArbolBinario, self).__init__()
		if(nodo.esRaiz()==False):
			raise ValueError('El nodo %s no es una raiz '%(nodo))
		self.__raiz__ = nodo


	def addNodo(self,nodo, nodoPadre, control):
			
		if nodoPadre == None:
			aux=self.__raiz__
		if nodoPadre != None and control == True:
			for hijo in nodoPadre:
				if hijo.esHoja():
					self.addNodo(nodo, hijo, False)
					return
			for hijo in nodoPadre:
				if len(hijo.getHijos()) != 2:
					self.addNodo(nodo, hijo, False)
					return 
			for hijo in nodoPadre:
				for hijito in hijo.getHijos():
					if hijito.esHoja():
						self.addNodo(nodo, hijito, False)
						return
				for hijito in hijo.getHijos():
					if len(hijito.getHijos()) != 2:
						self.addNodo(nodo, hijito, False)
						return 
		
		if nodoPadre != None and control != True:
			aux = nodoPadre

		if aux.esHoja():
			aux.addHijo(nodo)
		else:
			if len(aux.getHijos())!=2:
				aux.addHijo(nodo)
			else:
					hijos = aux.getHijos()
					self.addNodo(nodo, hijos, True)


	def __str__(self):
			pass	

















		