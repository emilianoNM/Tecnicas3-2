#!/usr/bin/env python
# coding: utf-8

# In[ ]:


num = 1
tmp = int(raw_input("..:Imprimir No. Multiplicados:..\n>Dame hasta que numero de imprimir: "))
h = 1
while num <= tmp:
    h *= num
    num += 1
print h

