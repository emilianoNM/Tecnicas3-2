import random
edges=[]

def guardar(lista):
    archivo = open("Grafica.txt","w")
    for i in lista:
        texto=str(i[0])
        for j in i[1:]:
            texto+=" "+str (j)
        texto+="\n"
        archivo.write(texto)
    archivo.close()
    return

def g_aristas(lista,aristas,i):
    n = int(random.uniform(0,aristas))
    if aristas==0:
        return
    for k in range(1,n):
        edge=int(random.uniform(1,len(lista)))
        if i not in edges and edge not in edges:
            edges.append(i)
            edges.append(edge)
            aristas=aristas-1
        if edge is not i and edge not in lista[i-1]:
            lista[i-1].append(edge)
            lista[edge-1].append(i)
    return aristas

def generador(vertices,aristas):
    aristas=aristas+1
    lista=[]
    for i in range(0,vertices):
        lista.append([])
        lista[i].append(i+1)   
    for i in range(1,vertices+1):
        aristas=g_aristas(lista,aristas,i)

    return lista

def main():
    lista=generador(100,40)
    print(lista)
    guardar(lista)
    return

main()
