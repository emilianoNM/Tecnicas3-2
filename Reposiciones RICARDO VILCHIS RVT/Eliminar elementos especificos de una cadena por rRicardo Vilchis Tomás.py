#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("programa que elimina elemntos especificos de una cadena ya establecida")
print("por Ricardo Viclhis Tomás")


# In[2]:


a = "abcdefghijklmnñopqrstuvwxyz"
b = "bdghkmnz"
for char in b:
    a = a.replace(char,"")
    print (a)

