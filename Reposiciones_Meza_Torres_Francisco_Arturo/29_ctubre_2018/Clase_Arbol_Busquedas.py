class Clase:
	def __init__(self, v):
		self.v= v

	a= Clase(3)
	a.__dict__
{’v’: 3}
a.__class__.__name__
’Clase

class Base:
	def __init__(self, v):
		self.v= v
		print "Inicializo la base con un %d" % v
	 def f1(self, n):
		return "f1 de la base recibe un %d" % n
	def f2(self, n):
		return "f2 de la base recibe un %d" % n

class Derivada(Base):
	def __init__(self, v):
		Base.__init__(self,v)
		print "Se ha inicializado la derivada con %d" % self.v
	def f2(self, n):
		return "f2 de la derivada recibe un %d" % n