#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def promedio():
    datos=[]
    print "..:Promedio:.."
    tmp = int(raw_input("> Dame la cantidad valores a promediar: "))
    for i in range(1,tmp+1):
        tmp2 = int(raw_input("> Dame el valor {}: ".format(i)))
        datos.append(tmp2)
    print "El promedio es: ",float(sum(datos))/float(len(datos))

promedio()

