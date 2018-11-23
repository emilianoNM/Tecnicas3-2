#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 10:18:48 2018

@author: israel
"""

#Producto de Numeros
num = 1
tmp = int(raw_input("..:Imprimir No. Multiplicados:..\n>Dame hasta que numero de imprimir: "))
h = 1
while num <= tmp:
    h *= num
    num += 1
print h