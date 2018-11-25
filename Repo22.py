#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Tabla de multiplicar
print "..:Tabla de Multiplicar:.."
def tablaMultiplicar():
    n = int(raw_input("Dame un numero a multplicar, rango [1,10]: "))
    for i in range(1,11):
        print n,"x",i,"=",n*i

tablaMultiplicar()

