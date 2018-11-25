#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def lenChar():
    lista = raw_input("..:Longitud de una cadena:..\n> Dame una palabra a contar: ")
    cont = 0
    for i in lista:
        cont += 1
    print "> La longitud es: {}".format(cont)
lenChar()

