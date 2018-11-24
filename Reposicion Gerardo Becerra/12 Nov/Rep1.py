
# coding: utf-8

# In[ ]:


#Gerardo Becerra

n = 1
num = input('Llegar hasta: ')
h = 0
suma = 0
while True:
    if 3*n > num:
        break
    if (3*n)%2 == 0:
        print 3*n,
        h += 1
        suma += 3*n
    n += 1
print '\nEntre 1 y %i hay %i numeros multiplos de 3 y de 2' % (num, h)
print 'Dichos numeros suman %i' % suma
 

