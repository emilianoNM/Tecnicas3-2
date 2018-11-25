#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Programa para saber si una cadena es un palindromo o no lo es")
print("Por Ricardo Vilchis Tomás")


# In[2]:


print("si la cadena es un palindromo el programa regresara el booleano true \n sino regresara false")
cadenita = input("Ingresa la cadena SIN TABULADOR PORFAVOR :C \n")
cadenita== ''.join(reversed(cadenita))

