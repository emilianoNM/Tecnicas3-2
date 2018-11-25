#----------
class Nodo:
    def __init__(self, t):
        self.llaves = list()
        self.hijos = list()
        self.hoja = 1
        self.n = 0
        for k in range(2 * t ):
            self.llaves.append([None])
        for k in range(2 * t +1 ):
            self.hijos.append([None])
#----------
class ArbolB():
    def __init__(self, gradoMinimo):
        self.t = gradoMinimo
        self.raiz = None
        
    def bTreeCreate(self):
        if (self.raiz == None):
            self.raiz = Nodo(self.t)
        return(self.raiz)
    
    def bTreeInsert(self, nodo, k):
        r = self.raiz
        if r.n == 2 * self.t - 1:
            
            s = Nodo(self.t)
            self.raiz = s
            s.hoja = 0
            s.n = 0
            s.hijos[1] = r
            self.bTreeSplitChild(s, 1)
            self.bTreeInsertNonFull(s, k)
        else:
            
            self.bTreeInsertNonFull(r, k)

    def bTreeInsertNonFull(self, x, k):
        i = x.n
        if x.hoja == 1:
            while (i >= 1) and (k < x.llaves[i]):
                x.llaves[i + 1] = x.llaves[i]
                i = i - 1
            x.llaves[i + 1] = k
            x.n = x.n + 1
        else:
            while (i >= 1) and (k < x.llaves[i]):
                i = i - 1
            i = i + 1
            if x.hijos[i].n == 2 * self.t - 1:
                self.bTreeSplitChild(x, i)
                if k > x.llaves[i]:
                    i = i + 1
            self.bTreeInsertNonFull(x.hijos[i], k)

    def bTreeSplitChild(self, x, i):
        z = Nodo(self.t)
        y = x.hijos[i]
        z.hoja = y.hoja
        z.n = self.t - 1
        
        for j in range(1, self.t):
            z.llaves[j] = y.llaves[j + self.t]
            y.llaves[j + self.t] = None
        
        if y.hoja == 0:
            for j in range(1, self.t + 1):
                z.hijos[j] = y.hijos[j + self.t]
                y.hijos[j + self.t] = None
        y.n = self.t - 1
        for j in range(x.n + 1, i, -1):
            x.hijos[j + 1] = x.hijos[j]
            
        x.hijos[i + 1] = z
        
        for j in range(x.n, i - 1, -1):
            x.llaves[j + 1] = x.llaves[j]

        x.llaves[i] = y.llaves[self.t]
        y.llaves[self.t] = None
        x.n = x.n + 1
    def imprimeNodo(self, nodo):
        for i in range(1, 2 + self.t, 1):
            if (nodo.llaves[i] != None and type(nodo.llaves[i]) !=list ):
                print(chr (nodo.llaves[i])," ",end='')
    #Entrada Nodo que se tomará como raiz
    #Salida Impresion en pantalla de las llaves del nodo padre y de los hijos
    def imprimeRaiz(self,r):
        #Verificamos si la raiz que estamos tomando tiene hijos, de ser asi sigue con el proceso
        #de otro modo termina la funcion
        if r.hijos.count([None]) == 2 * self.t +1 :
            return
        #Imprime las llaves del nodo padre
        print("Llaves nodo Padre \t\t ",end='')
        self.imprimeNodo(r)
        print("\n")
        #Imprime las llaves de los nodos hijos
        print("Llaves nodos Hijos \t",end='')
        #Recorre la lista de hijos e imprime los nodos validos
        for i in range(1, 2 * self.t +1):
            #Verifica si el nodo no es un objeto nulo y si no es una lista del tipo [None]
            if r.hijos[i] != None and type (r.hijos[i]) != list :
            #Este if solo es para darle formato a la salida
                if i!=1:
                    print("<---> ",end='')
            #Mandamos a llamar al metodo imprimeNodo donde imprime las llaves
                self.imprimeNodo(r.hijos[i])
        print("\n")
        #Al término de esto llamamos recursivamente el metodo de
        #imprimeRaiz dando como parametro todos los nodos validos, siendo asi
        #Un recorrido tipo inOrden en el contexto de árboles binarios
        for j in range(1,2 * self.t +1 ):
            #Verificamos si los nodos son validos (diferente de None y de [None])
            if r.hijos[j] != None and type (r.hijos[j]) != list :
                self.imprimeRaiz(r.hijos[j])      
        return
    #Entrada: Nodo Raiz y Llave a Buscar:
    #Salida: Mensaje notificando si se encontró la llave
    def bTreeSearch(self,x,k):
        i=1
        #Verifica si la llave es mayor que las llaves que contiene el nodo
        #Nos da un indice con el cual podremos ir al siguiente nodo en busca de la llave
        while (i<= x.n and k>x.llaves[i]):
            i+=1
        #Si en la posicion del indice, la llave coincide con el elemento
        #De la lista de llaves, regresa el mensaje y termina la funcion
        if i<= x.n and k>=x.llaves[i]:
            print("Se encontró la llave ",chr(k))
            return
        else:
            #Si en el nodo no se encontró la llave, verifica si es una hoja,
            #En caso de que sea una hoja, termina la funcion ya que no encontró el valor
            #de otro modo se manda a llamar de manera recursiva con el indice del último hijo
            #correspondiente
            if x.hoja ==1:
                print("No se encontro la llave ",chr(k))
                return
            else:
                self.bTreeSearch(x.hijos[i],k)
        return
    
class Controladora:
    def main(self):
        #L=['B','T','H','M']
        L=['O','C','Z', 'G', 'L', 'E', 'N', 'P', 'R', 'D', 'J', 'Q', 'F', 'W', 'X']
        arbol = ArbolB(2)
        r=arbol.bTreeCreate()
        for i in L:
            arbol.bTreeInsert(r,ord(i) )
        r=arbol.raiz
        arbol.imprimeRaiz(r)
        arbol.bTreeSearch(r,ord('C'))
        return
def main():
    c = Controladora()
    c.main()
    return

main()
