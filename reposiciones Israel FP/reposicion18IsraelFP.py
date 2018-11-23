#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 11:40:52 2018

@author: israel
"""

#Contador de Vocales
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