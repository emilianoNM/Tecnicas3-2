#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Creado por RVT")
print("Programa que verifica si una lista cotiene SOLO digitos o no ")


# In[2]:


a = input("ingresa digitos o texto papau")
[k for k in a if k.isdigit()]
['1', '2', '3']
print("SI el resultado es TRUE significa que la lista contiene solo digitos")
a.isdigit()

