#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 18:03:56 2018

@author: israel
"""
# Positivo o Negativo
def posNeg(num):
    if num > 0:
        print "El numero dado: ",num," es positivo"
    elif num < 0:
        print "El numero dado: ",num," es negativo"
    else:
        print "> Dame un numero diferente de cero"
print "..: Positivo o Negativo:.."
tmp = int(raw_input("> Confirmo si el numero es positivo o negativo: "))
posNeg(tmp)
