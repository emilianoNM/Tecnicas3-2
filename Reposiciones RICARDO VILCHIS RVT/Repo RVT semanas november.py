class Vertice:
    def __init__(self,n):
        self.nombre = n
        self.vecinos=list()
        self.distancia = 9999
        self.color = 'white'
        self.padre =-1
    def agregarVecino(self,v):
        if v not in self.vecinos:
            self.vecinos.append(v)
            self.vecinos.sort()
class Grafica:
    vertices = {}
    tiempo = 0
    def agregarVertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre] = vertice
            return(True)
        else:
            return(False)
    def agregarAristas(self,u,v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.agregarVecino(v)
                if key == v:
                    value.agregarVecino(u)
            return(True)
        else:
            return(False)
    def imprimirGrafica(self):
        for key in sorted(list(self.vertices.keys())):
            print("Vertice: " + key)
            print("Descubierto/Termino: " + str(self.vertices[key].d) + "/" + str(self.vertices[key].f))
    def dfs(self, vert):
        global tiempo
        tiempo = 0
        if self.vertices[vert.nombre].color == 'white':
            self.dfsVisitar(self.vertices[vert.nombre])
        
    def dfsVisitar(self, vert):
        global tiempo
        tiempo = tiempo + 1
        vert.d = tiempo
        vert.color = 'gray'
    
        for v in vert.vecinos:
            if self.vertices[v].color == 'white':
                self.vertices[v].pred = vert
                self.dfsVisitar(self.vertices[v])
        vert.color = 'black'
        tiempo = tiempo + 1
        vert.f = tiempo

class Controladora:
    def main(self):
        g=Grafica()
        a = Vertice("A")
        g.agregarVertice(a)

        for i in range(ord('A'),ord('K')):
            g.agregarVertice(Vertice(chr(i)))

        edges = ['AB','AE','BF','CG','DE','DH','EH','FG','FI','FJ','GJ']

        for edge in edges:
            g.agregarAristas(edge[:1],edge[1:])

        g.dfs(a)
        g.imprimirGrafica()

def main():
    c = Controladora()
    c.main()
    return

main()
