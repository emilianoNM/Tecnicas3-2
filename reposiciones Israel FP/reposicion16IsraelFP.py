#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 11:30:20 2018

@author: israel
"""
#Numero mayor
def maxNum():
    n1 = int(raw_input("..:Numero Mayor:..\n> Dame un numero a comparar: "))
    n2 = int(raw_input("> Dame el segundo numero a comparar: "))
    if n1 < n2: print "> {} es Mayor".format(n2)
    elif n1 > n2: print "> {} es Mayor".format(n1)
    else: print "> Son iguales"
maxNum()