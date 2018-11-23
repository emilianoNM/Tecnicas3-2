#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 10:55:43 2018

@author: israel
"""

#Multiplos
def multiplo():
    num = int(raw_input("\n..:Multiplo:..\n> Dame el numero para encontrar su multiplo [1,100]: "))
    if num == 0:
        print "Error, el numero debe ser diferente de cero"
        return None
    i = 1
    h = 0
    while i <= 100:
        if  i % num == 0:
            print i
            h += 1
        i += 1
    print "Entre 1 a 100 se tienen {} multiplos de {}".format(h,num)

multiplo()
        