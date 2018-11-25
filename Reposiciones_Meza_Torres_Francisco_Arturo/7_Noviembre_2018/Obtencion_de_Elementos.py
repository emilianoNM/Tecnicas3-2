#!/usr/bin/env python
from types import *
from math import *

class IntSet:
	def __init__(self): # inicializaci´on
		self.c = 0L

def __str__(self): # impresi´on del resultado
	c = self.c
	s = "{ "
	i = 0
	while c != 0:
		j = 2**long(i)
		if c & j:
			s = s + str(i) + ’ ’
			c = c - j
		i = i + 1
	s = s + "}"
	return s

# inserci´on de un entero o
# de una lista de enteros

def insert(self, n):
	if type(n) != ListType:
		self.c = self.c | 2**long(n)
	else:
		for i in n:
			self.c = self.c | 2**long(i)
def __len__(self):
	c = self.c
	i = 0
	n = 0
	while c != 0:
		j = 2**long(i)
		if c & j:
			c = c - j
			n = n + 1
		i = i + 1
return n