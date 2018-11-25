#!/usr/bin/env python
# coding: utf-8

# In[15]:


print("Programa Laberinto raton")
print("Hecho en EDA y modificado para tecnicas")
pila=[(17,0)]
visitados=[(17,0)]


# In[16]:


laberinto = (('x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' '),

('x',' ','x',' ','x','x','x','x','x',' ','x',' '),

('x',' ','x',' ','x',' ',' ',' ',' ',' ','x',' '),

('x',' ','x',' ','x',' ','x',' ','x','x',' ',' '),

(' ',' ',' ',' ','x',' ','x','x','x','x',' ',' '),

('x',' ','x',' ','x',' ',' ',' ','x',' ',' ','x'),

('x',' ','x',' ','x',' ','x',' ','x','x',' ','x'),

('x',' ','x',' ','x','x','x',' ','x',' ',' ','x'),

('x',' ',' ',' ',' ',' ',' ',' ','x','x',' ','x'),

('x','x','x',' ','x','x','x','x','x',' ',' ',' '),

('x','x','x',' ','x',' ','x','x','x',' ','x',' '),

(' ','x','x',' ','x',' ','x',' ',' ',' ','x',' '),

(' ','x','x',' ','x',' ','x','x','x',' ','x',' '),

(' ','x','x',' ','x',' ',' ',' ',' ',' ',' ',' '),

(' ',' ',' ',' ','x','x','x','x','x','x','x','x'),

(' ','x','x',' ','x','x','x',' ','x',' ','x',' '),

(' ','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' '),

(' ','x','x',' ','x','x','x',' ','x','x','x','x'))


# In[17]:


laberinto


# In[18]:


def imprimelaberinto(x,raton,salida):
    raton=(17,0)
    salida=(0,4)
    k=0
    while k<len(x):
        print(x[k])
        k=k+1
        


# In[19]:


imprimelaberinto(laberinto,(1,4),(5,3))


# In[20]:


def push(pila,p):
    pila.append(p)
    return pila
def pop(pila):
    if len(pila)>0:
        pila.pop()
        return pila
    return("La pila se encuentra vacia")
def tos(pila):
    x = len(pila)
    tos = pila[x-1]
    return tos


# In[21]:


#En este punto ya probe "try" y "except" solo que las borre


# In[22]:


def visitado(pos):
    k=0
    while k<len(visitados):
        if pos==visitados[k]:
            return True
            k=k+1
        k=k+1
    while k==len(visitados):
        return False
        k=k+1


# In[23]:


#En este punto ya probe el correcto funcionamiento de mi funcion visitado


# In[24]:


def camino(pos):
    i=pos[0]
    j=pos[1]
    if laberinto[i][j]== " " and i>=0 and j>=0:
        return True
    elif laberinto[i][j]== "x" and i>=0 and j>=0:
        return False


# In[25]:


#En este punto ya probe el correcto funcionamiento de mi funcion camino


# In[26]:


def movimiento(raton):
    i=raton[0]
    j=raton[1]
    if camino((i-1,j))==True and visitado((i-1,j))==False:
        raton=((i-1,j))
        push(visitados,((i-1,j)))
        push(pila,((i-1,j)))
        print(visitados)
        print(pila)
        return raton #Asi se mueve hacia arriba si el laberinto se lo permite
    elif camino((i+1,j))==True and visitado((i+1,j))==False:
        raton=((i+1,j))
        push(visitados,((i+1,j)))
        push(pila,((i+1,j)))
        print(visitados)
        print(pila)
        return raton #Asi se mueve hacia abajo si el laberinto se lo permite
    elif camino((i,j+1))==True and visitado((i,j+1))==False:
        raton=((i,j+1))
        push(visitados,((i,j+1)))
        push(pila,((i,j+1)))
        print(visitados)
        print(pila)
        return raton #Asi se mueve hacia la derecha si el laberinto se lo permite
    elif camino((i,j-1))==True and visitado((i,j-1))==False:
        raton=((i,j-1))
        push(visitados,((i,j-1)))
        push(pila,((i,j-1)))
        print(visitados)
        print(pila)
        return raton #Asi se mueve hacia la izquierda si el laberinto se lo permite
        
        

            
    
    


# In[27]:


def main():
    raton=(17,0)
    salida=(0,4)
    #Como pila y visitados las declare globalmente, desde un principio llene a pila y visitados con la posicion del raton
    a=2
    while a==2:
        movimiento(raton)
        #Tuve que borrar mucho de lo que habia puesto en main porque me abortaba el
        #programa pero era por el main, porque lo anterior estaba bien hecho
    


# In[ ]:




