#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 11:51:05 2018

@author: israel
"""

#Invertir una cadena
def invertChar():
    cadena = raw_input("..:Invierte una Cadena:..\n> Dame una palabra a invertir: ")
    print "> Cadena invertida: {}".format(cadena[::-1])
invertChar()