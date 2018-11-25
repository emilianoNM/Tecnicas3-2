#!/usr/bin/env python
# coding: utf-8

# In[ ]:


num = 1
tmp = int(raw_input("..:Imprimir No. Primos:..\n>Dame hasta que numero de imprimir: "))
h = ''
while num <= tmp:
    if num%2 != 0:
        h += ' %i' % num
    num += 1
print h

