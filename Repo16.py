#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def maxNum():
    n1 = int(raw_input("..:Numero Mayor:..\n> Dame un numero a comparar: "))
    n2 = int(raw_input("> Dame el segundo numero a comparar: "))
    if n1 < n2: print "> {} es Mayor".format(n2)
    elif n1 > n2: print "> {} es Mayor".format(n1)
    else: print "> Son iguales"
maxNum()

