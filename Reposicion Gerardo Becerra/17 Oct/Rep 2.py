#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print "Inscripcion en el curso 04 de 75.40"
    padron=input("Ingresa un padrón (<=0 para terminar): ")

ins = []
while padron > 0:

        ins.append(padron)

        padron=input("Ingresá un padrón (<=0 para terminar): ")

print "Esta es la lista de inscriptos: ", ins

