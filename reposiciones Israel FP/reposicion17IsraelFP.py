#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 11:35:12 2018

@author: israel
"""

# Longitud de una cadena
def lenChar():
    lista = raw_input("..:Longitud de una cadena:..\n> Dame una palabra a contar: ")
    cont = 0
    for i in lista:
        cont += 1
    print "> La longitud es: {}".format(cont)
lenChar()
