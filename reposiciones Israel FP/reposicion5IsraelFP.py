#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:53:29 2018

@author: israel
"""
#Lanzar moneda
import random
def coinRand():
    coin = random.randint(1,2)
    if coin == 1:
        print "Aguila"
    elif coin == 2:
        print "Sol"

tmp = int(raw_input(">Dame las veces que se lanzara la moneda: "))
for i in range(tmp):
    coinRand()
