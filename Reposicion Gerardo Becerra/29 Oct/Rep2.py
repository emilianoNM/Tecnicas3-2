
# coding: utf-8

# In[ ]:


def msertionSort (alist):
    for índex in range(1,len(alist)):

        currentvalue = alist[índex]
        position = Índex

    while position>0 and alist[position-1]>currentvalue:
        alist[position]=alist[position-1]
        position = position-1

    alist [position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print (alist)

