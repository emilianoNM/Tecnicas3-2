#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def contVocal():
    cadena = raw_input("..:Contador de Vocales:..\n> Dame una palabra a contar: ")
    cadena = cadena.lower()
    vocales = "aeiou"

    for i in vocales:
        cont = 0
        for j in cadena:
            if i == j:
                cont += 1
        print "Hay {} de la vocal {} ".format(i,cont)
contVocal()

