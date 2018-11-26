#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = 100
h = 0
while n >= 1:
    if n%2 != 0:
        print n,
        h += n
    n -= 1
print 'y su suma es: %i' % h

