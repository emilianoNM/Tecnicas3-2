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
		return str(self.id) 
	def __repr__(self):
		return str(self.id)
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

	def addNodo(self,nodo,nodoSiguiente=None):
			if nodoSiguiente==None :
    				aux=self.__raiz__
			else :
    				aux=nodoSiguiente
			if aux.esHoja():
				aux.addHijo(nodo)
			else:
				if len(aux.getHijos())!=2:
					aux.addHijo(nodo)
				else:
					hijos=aux.getHijos()
					for hijo in hijos:
						if hijo.esHoja():
							hijo.addHijo(nodo)
							return 
					for hijo in hijos:
						if len(hijo.getHijos())!=2:
							hijo.addHijo(nodo)
							return
					
					for hijo in hijo.getHijos():
    						self.addNodo(nodo,hijo)
						return
							
					
	def __str__(self):
		self.recorrerNodo(self.__raiz__)

	def recorrerNodo(self,nodo,profundidad=1):
		print "     "*profundidad+str(nodo)
		hijos=nodo.getHijos()
		for hijo in hijos:
			self.recorrerNodo(hijo,profundidad+1)


















		
