#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 23:50:17 2018

@author: israel
"""

#Ordenar alfabeticamente una cadena

palabra = raw_input("\n..:Ordenar Alfabeticamente:..\n>Dame la palabra (solo minusculas): ")
convertido = list(palabra)
convertido = convertido.sort()
print convertido
