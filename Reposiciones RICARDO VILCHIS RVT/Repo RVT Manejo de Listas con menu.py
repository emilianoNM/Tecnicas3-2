#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Creado por RVT")
print("Manejo de listas con MArio bros")

print("Bienvenido a Super Mario World!!")
print("Eres el player1  :D")


# In[2]:


personajes=["Mario", 100, 30, 20, 3000, "saltar y nadar"],["Joshi", 70, 40, 10, 300, "volar"],["Toad", 80, 10, 50, 200, "N/A"],["Luigi", 95, 35, 18, 3200,  "super salto"],["Peach",115, 40, 10, 1500, "flotar"]
 


# In[3]:


a=personajes[0]


# In[4]:


def menu(opciones):
    salir= False
    while not salir:
        k=1
        for op in opciones:
            print(k," : ",op)
            k = k+1
        print(k," : Salir")
        sel = int(input("Opcion?"))
        salir = sel > 0 and sel<=k
    print("Elegiste la opcion ",sel)
    return sel

    


# In[5]:


def listarpersonajes():
    global personajes
    for p in personajes:
        print(p)
    return


# In[6]:


def personajeactual():
    global personajes
    global a
    print("Tu personaje actual es:", a)
    
    
    return 
    
    


# In[7]:


def buscarpersonaje():
    global personajes
    global c
    global a
    
    nombre=input("Dame el nombre del personaje que quieres buscar")
    k=0
    while(k<=4):
        s=personajes[k]
        if nombre==s[0]:
            print("Personaje encontrado en base de datos de Super Mario, te lo mostramos a continuacion :D")
            c=personajes[k]
            print(c)
        k=k+1
    if nombre!=c[0]:
        print("Este personaje no existe dentro del juego x_x")
    else: 
        np=int(input("Quieres seleccionar este personaje como personaje actual? 1.-si \n 2.- NO"))
        if np==1:
            a=c
            print("Tu nuevo personaje es ", a)
            
            
        else:
            print("Tu personaje actual sigue siendo el mismo")
            
            
       
        
    
   
    return 


# In[8]:


def navegarporlista():
    global personajes
    global a
    print("Bienvenido al navegador de la lista de personajes")
    print("Presiona S si quieres ver el siguiente personaje")
    print("Presiona A si quieres ver el anterior personaje")
    print("Presiona I para ver el primer personaje de la lista")
    print("Presiona F si quieres ver el ultimo personaje de la lista")
    print("Presiona U para elegir al personaje mostrado")
    print("Presiona T para volver a la lista")
    k=0
    print("El personaje actual es ", personajes[k])
    x=input("Dame la opcion que desees")
    while(x=='S' or x=='A' or x=='I' or x=='F' or x=='U' or x=='T'):
        if x=='S' :
            if (k+1)==5:
                print("No hay personaje posterior a este en el juego x_x")
                x=input("Dame la opcion que desees")
                
                
            elif (k+1)!=5:
                print("El siguiente personaje es:" ,personajes[k+1])
                x=input("Dame la opcion que desees")
                k=k+1
            
        elif x=='A':
            if (k-1)==-1:
                print("No hay personaje anterior a este en el juego x_x")
                x=input("Dame la opcion que desees")
                
            elif (k-1)!=-1:
                print("El anterior personaje es:" ,personajes[k-1])
                x=input("Dame la opcion que desees")
                k=k-1
                
        elif x=='I':
            print("El primer personaje de la lista es:" , personajes[0])
            x=input("Dame la opcion que desees")
            
        elif x=='F':
            print("EL ultimo personaje de la lista es :", personajes[4])
            x=input("Dame la opcion que desees")
            
        elif x=='U':
            a=personajes[k]
            print("Tu nuevo personaje es: " ,a)
            x=input("Dame la opcion que desees")
            
               
        else:
            if x=='T':
                print("Volveras al menu principal ")
                return
        
        


# In[9]:


def main():
    op=0
    while op!=6:
        op=menu(["Mostrar lista de personajes", "Personaje actualmente elegido","Buscar un personaje por nombre", "Navegar por la lista"])
        if op==1:
            listarpersonajes()
        elif op==2:
            personajeactual()
        elif op==3:
            buscarpersonaje()
        elif op==4:
            navegarporlista()
        else:
            if op==5:
                print("Decidiste salir del programa, bye bye")
                break
    return


# In[ ]:


main()


# In[ ]:





# In[ ]:




