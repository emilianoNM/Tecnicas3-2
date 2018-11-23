li=int(input("escribe rango mas bajo"))
ls=int(input("escribe rango mas algo"))
a=[]
a=[x for x in range(1,ls+1) if (int(x**.5))**2==x and sum(lis(map(int,str(x))))<10]
