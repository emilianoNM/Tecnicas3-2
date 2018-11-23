#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 11:53:16 2018

@author: israel
"""

#Binario - decimal
def binDecimal():
    decimal = int(raw_input("..:Decimal a Binario:..\n> Dame el numero a convertir: "))
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal%2) + binario
        decimal = decimal // 2
    print "> Forma binaria: ", str(decimal) + binario
binDecimal()