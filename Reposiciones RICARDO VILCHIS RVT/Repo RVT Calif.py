#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Calificaciones RVT")


# In[ ]:


print("Ingrese las califiacones de los 3 parciales realizados en el semestre")
a=int(input())
b=int(input())
c=int(input())
calificacionpromediofinal=(a+b+c)/3
if(calificacionpromediofinal>=6):
    print("EL ALUMNO APROBO ESTA MATERIA :D")
elif(calificacionpromediofinal<6):
    print("REROBADO HIJO :d")

