import math

#----------
class Nodo:
    def __init__(self, valor):
        self.hijoIzq = None
        self.hijoDer = None
        self.val = valor
#----------
class Arbol:
    #Creamos una lista auxiliar donde se iran guardando los nodos para su analisis
    nodos=list()
    h=0
    c=0
    def __init__(self):
        self.raiz = None
    def obtenerRaiz(self):
        return(self.raiz)
    def agregar(self, val):
        if (self.raiz == None):
            self.raiz = Nodo(val)
        else:
            self.agregarNodo(val, self.raiz)
    def agregarNodo(self, val, nodo):
        if (val < nodo.val):
            if (nodo.hijoIzq != None):
                self.agregarNodo(val, nodo.hijoIzq)
            else:
                nodo.hijoIzq = Nodo(val)
        else:
            if (nodo.hijoDer != None):
                self.agregarNodo(val, nodo.hijoDer)
            else:
                nodo.hijoDer = Nodo(val)
    def preorden(self, nodo):
        if (nodo != None):
            print(str(nodo.val))
            if (nodo.hijoIzq != None):
                self.preorden(nodo.hijoIzq)
            if (nodo.hijoDer != None):
                self.preorden(nodo.hijoDer)
    def imprimePreorden(self):
        if (self.raiz != None):
            self.preorden(self.raiz)
    def inOrden(self,nodo):
        if nodo!=None:
            if nodo.hijoIzq!=None:
                self.inOrden(nodo.hijoIzq)
            print(str(nodo.val))
            if nodo.hijoDer !=None:
                self.inOrden(nodo.hijoDer)
    def imprimeInOrden(self):
        if(self.raiz!=None):
            self.inOrden(self.raiz)
            
    def postOrden(self,nodo):
        if nodo!=None:
            if nodo.hijoIzq!=None:
                self.postOrden(nodo.hijoIzq)
            if nodo.hijoDer !=None:
                self.postOrden(nodo.hijoDer)
            print(str(nodo.val))
    def imprimePostOrden(self):
        if(self.raiz!=None):
            self.postOrden(self.raiz)
    def explorar(self,nodo):
        global h
        global c
        
        if nodo == self.raiz:
            h=0
            c=0
        if nodo.hijoIzq not in self.nodos or nodo.hijoDer not in self.nodos:
            if nodo.hijoIzq != None:
                self.nodos.append(nodo.hijoIzq)
            if nodo.hijoDer != None:
                self.nodos.append(nodo.hijoDer)
            c+=1
        
        if nodo.hijoIzq != None:
            self.explorar(nodo.hijoIzq)
        if nodo == self.raiz:
            c=1
        if nodo.hijoDer != None:
            self.explorar(nodo.hijoDer)
        if c>=h:
            h=c
        return h
    def dfs(self):
        self.nodos.append(self.raiz)
        self.nodos.append(None)
        h=0
        if self.raiz != None:
            h=self.explorar(self.raiz)
        return h
    

def main():
    h=0
    arbol = Arbol()
    #arbol2 = Arbol()
    #L=[10, 5, 20, 3, 7, 25]
    L=[3, 5, 7, 10, 20, 25]
    #L=[25,20,10,7,5,3]
    print("Arbol 1")
    print(L)
    for i in L:
        arbol.agregar(i)
    print("-----------")
    print("PreOrden")
    print("-----------")
    arbol.imprimePreorden()
    print("-----------")
    print("InOrden")
    print("-----------")
    arbol.imprimeInOrden()
    print("-----------")
    print("PostOrden")
    print("-----------")
    arbol.imprimePostOrden()
    h=arbol.dfs()
    print("-----------")
    print("Altura del Árbol ", h)
    hojas=0
    for i in arbol.nodos:
        if i != None:
            if i.hijoDer is None and i.hijoIzq is None:
                hojas+=1
    print("Hojas ", hojas)

    return

main()
