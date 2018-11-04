#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Arbol.py

#GerardoBecerra

class nodo(object):
	def __init__(self,id,padre):
		super(nodo,self).__init__()
		self.id=id
		self.padre=padre
		self.hijos=[]
		if padre!=None:
			padre.addhijo(self)
            
    def addhijo(self,hijo):
		self.hijos.append(hijo)
		hijo.padre=self
        
    def eshoja(self):
		return len(self.hijos)==0
    
    def gethijos(self):
		return self.id
    
    def esraiz(self):
		return self.padre==None
    
	def __str__(self):
		return self.id 
    
	def __repr__(self):
		return self.id

        
class ArbolBinario(object):
	def __init__(self,nodo):
		super(ArbolBinario,self).__init__()
		if(nodo.esraiz()==False):
			raise ValueError('El nodo no es una raiz')
		self.__raiz__=nodo
        
	def addNodo(self,nodo, nodoPadre, control):
			
		if nodoPadre == None:
			aux=self.__raiz__
		if nodoPadre != None == True:
			for hijo in nodoPadre:
				if hijo.eshoja():
					self.addNodo(nodo, hijo, False)
					return
			for hijo in nodoPadre:
				if len(hijo.gethijos()) != 2:
					self.addNodo(nodo, hijo, False)
					return 
			for hijo in nodoPadre:
				for hijo2 in hijo.gethijos():
					if hijo2.eshoja():
						self.addNodo(nodo, hijo2, False)
						return
				for hijo2 in hijo.gethijos():
					if len(hijo2.gethijos()) != 2:
						self.addNodo(nodo, hijo2, False)
						return 
		
		if nodoPadre != None:
			aux = nodoPadre

		if aux.eshoja():
			aux.addhijo(nodo)
		else:
			if len(aux.gethijos())!=2:
				aux.addhijo(nodo)
			else:
					hijos = aux.gethijos()
					self.addNodo(nodo, hijos, True)
                    
    def __str__(self):
			pass

