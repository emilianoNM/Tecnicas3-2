class nodo(object):
	def __init__(self,id,padre):
		super(nodo,self).__init__()
		self.id=id
		self.padre=padre
		self.hijos=[]
		if padre!=None:
			padre.addhijo(self)

"""	def add(self,nodo):
		hijos=nodo.gethijos()
		for hijo in hijos:
			if hijo.eshoja():
				hijo.addhijo(nodo)
				return
			elif len(hijo.gethijos())!=2:
				hijo.addhijo(nodo)
				return
			else:
				hijo.add(hijo)

		pass

"""
	def addhijo(self,hijo):
		self.hijos.append(hijo)
		hijo.padre=self

	def eshoja(self):
		return len(self.hijos)==0

	def delete(self):
		if (self.esraiz()):
			pass
		else:
			padre=self.padre
			hijos=padre.gethijos()
			hijos.remove(self)
			self.padre=None

		self.hijos=None
	

	def esraiz(self):
		return self.padre==None

	def gethijos(self):
		return self.hijos

	def __str__(self):
		return self.id

	def __repr__(self):
		return self.id

class arista(object):
	def __init__(self,arg):
		super(arista,self).__init__()
		self.arg=arg

class arbol(object):
	def __init__(self,arg):
		super(arbol,self).__init__()
		self.arg=arg

class arbolbinario(object):
	def __init__(self,nodo):
		super(arbolbinario,self).__init__()
		if(nodo.esraiz()==False):
			raise ValueError('El nodo no es una raiz')
		self.__raiz__=nodo
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

#			self.addhijo(nodo,raiz)	

		#	while aux.eshoja()==False:

			#pass

		


	def __str__():
		pass