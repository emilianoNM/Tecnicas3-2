#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 12:05:42 2018

@author: israel
"""
#Mostrar Caracteres de una Cadena
def printCad():
    cadena = raw_input("..:Caracteres de una Cadena:..\n> Dame una palabra: ")
    for i in cadena:
        print i
        
printCad()