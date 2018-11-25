#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Repo RVT")
print("Programa que identifique las vocales de una cadena")


# In[2]:


def vocales(x):
    x=0
    total=0
    for vocal in c:
        if ('a' in c):
            x=x+1
        if 'e' in c:
            x=x+1
        if 'i' in c:
            x=x+1
        if 'o' in c:
            x=x+1
        if 'u' in c:
            x=x+1
           
    return x

c=input("Ingresa la cadena a la cual evaluaras cuantas vocales tiene papaw\n")
print (vocales(c))

