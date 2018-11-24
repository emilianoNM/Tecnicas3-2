#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a = input('Primer valor: ')
b = input('Segundo valor: ')
n = 10
suma = 0
sumas = 0
if a >= b:
    while n <= 50:
        suma += n
        n += 4
    print suma
if a/b <= 30:
    sumas = (a**2+b**2)
    print sumas

