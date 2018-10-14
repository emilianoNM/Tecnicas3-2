#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 13:27:59 2018

@author: israel
"""
class Nodo:
    def __init__(self,valor):
        self.hijoIzq = None
        self.hijoDer = None
        self.val = valor
    def isLeaf(self):
        if(self.hijoIzq == None and self.hijoDer == None):
            return False

class Arbol:

    def __init__(self):
        self.__raiz__ = None
    
    def obtenerRaiz(self):
        return self.__raiz__
    
    def agregar(self,val):
        if(self.__raiz__ == None):
            self.__raiz__ = Nodo(val)

        else:
            self.agregarNodo(val,self.__raiz__)
    
    def agregarNodo(self,val,nodo):
        if(val < nodo.val):
            if(nodo.hijoIzq!=None):
                self.agregarNodo(val,nodo.hijoIzq)
            else:
                nodo.hijoIzq = Nodo(val)
                
        else:
            if(nodo.hijoDer!=None):
                self.agregarNodo(val,nodo.hijoDer)
            else:
                nodo.hijoDer = Nodo(val)

def printTree(nodo):
    if(nodo == None):
        return
    printTree(nodo.hijoIzq)
    print "[",nodo.val,"]",
    printTree(nodo.hijoDer)
    
    
"""def traverse(nodo):
    thislevel = [nodo]
    while thislevel:
        nextlevel = list()
        for n in thislevel:
            print "[",n.val,"]",
            if n.hijoIzq: nextlevel.append(n.hijoIzq)
            if n.hijoDer: nextlevel.append(n.hijoDer)
        print
        thislevel = nextlevel"""
            

d=Arbol()
d.agregar(1)
d.agregar(2)
d.agregar(3)
d.agregar(3)
d.agregar(5)
d.agregar(6)
d.agregar(5)
d.agregar(8)
d.agregar(9)

printTree(d.__raiz__)