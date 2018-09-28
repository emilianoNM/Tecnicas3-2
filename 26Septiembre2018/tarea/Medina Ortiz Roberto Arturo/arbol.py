class nodo(object):
	def __init__(self,id,padre):
		super(nodo,self).__init__()
		self.id=id
		self.padre=padre
		self.hijos=[]
		if padre!=None:
			padre.addhijo(self)

	def add(self,nodo):
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
	def addnodo(self,nodo):
		aux=self.__raiz__
		aux.add(nodo)

		"""if aux.eshoja():
			aux.addhijo(nodo)
		elif len(aux.gethijos())!=2:
			aux.addhijo(nodo)
		else:
			hijos=aux.gethijos()
			for hijo in hijos:
				if hijo.eshoja():
					hijo.addhijo(nodo)
					return
				elif len(hijo.gethijos())!=2:
					hijo.addhijo(nodo)
					return
				else:
					hijos=aux.gethijos()
					for hijo in hijos:
						if hijo.eshoja():
							hijo.addhijo(nodo)
							return
						elif len(hijo.gethijos())!=2:
							hijo.addhijo(nodo)
							return
						else:
							hijos=aux.gethijos()
							for hijo in hijos:
								if hijo.eshoja():
									hijo.addhijo(nodo)
									return
								elif len(hijo.gethijos())!=2:
									hijo.addhijo(nodo)
									return
								else:
									pass
	

#			self.addhijo(nodo,raiz)	

		#	while aux.eshoja()==False:

			#pass

		pass
		"""


	def __str__():
		pass