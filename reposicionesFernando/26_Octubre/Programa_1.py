#Este Programa toma el numero de elementos y genera un numero aleatorio del 1 al 20

import random #Aqui importo la libreria 
a=[]
n=int(input("Porfavor escriba el numero de elementos"))
for j in range(n):
    a.append(random.randint(1,20))
print('La lista aleatoria es:',a)