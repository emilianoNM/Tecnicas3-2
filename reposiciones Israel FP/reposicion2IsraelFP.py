#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:36:00 2018

@author: israel
"""
#Tabla de multiplicar
print "..:Tabla de Multiplicar:.."
def tablaMultiplicar():
    n = int(raw_input("Dame un numero a multplicar, rango [1,10]: "))
    for i in range(1,11):
        print n,"x",i,"=",n*i

tablaMultiplicar()