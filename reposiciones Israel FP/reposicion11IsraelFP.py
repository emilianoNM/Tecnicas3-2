#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 10:03:53 2018

@author: israel
"""

#Imprime No. primos
num = 1
tmp = int(raw_input("..:Imprimir No. Primos:..\n>Dame hasta que numero de imprimir: "))
h = ''
while num <= tmp:
    if num%2 != 0:
        h += ' %i' % num
    num += 1
print h
        