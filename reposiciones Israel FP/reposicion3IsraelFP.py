#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:45:36 2018

@author: israel
"""
#Area del Circulo
def areaCirculo():
    print "..:Area del Circulo:.."
    tmp = int(raw_input(">Dame el radio del circulo: "))
    print "> El area del circulo es: ", (3.1416) * tmp * tmp

areaCirculo()