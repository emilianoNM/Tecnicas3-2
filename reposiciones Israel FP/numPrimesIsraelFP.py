#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 14:05:51 2018

@author: israel
"""

def numPrimo(num):
#    El numero tiene que divisirse:
#    1.- divisble entre 1
#    2.- divisible entre si mismo
    for i in range(2,num):
        if(num%i)==0:
            return False
    return True

while True:
    try:
        dato = int(raw_input("> Inserta un numero, escribe '0' para <salir>: "))
        if dato == 0: break
        if numPrimo(dato): print "\nEl numero %s, es primo" % dato
        else: print "\n EL numero %s, no es primo" % dato
    except:
        print "\n> El numero tiene que ser entero"
            