#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 10:47:05 2018

@author: israel
"""

#Sumatoria 1 - n (numeros)
def suma(num):
    return (num * (num+1))/2

tmp = int(raw_input("..:Sumatoria hasta N numeros:..\n> Dame hasta que numero de imprimir [1-N]: "))
print "> Resultado: ", suma(tmp)
