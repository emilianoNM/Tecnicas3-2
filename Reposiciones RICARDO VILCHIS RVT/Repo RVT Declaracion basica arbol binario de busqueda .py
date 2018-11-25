#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Declaracion basica de un arbol binarioo de busqueda")
print("Por RVT")


# In[2]:


class ArbolBinario:

    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def longitud(self):
        return self.tamano

    def __len__(self):
        return self.tamano

    def __iter__(self):
        return self.raiz.__iter__()

