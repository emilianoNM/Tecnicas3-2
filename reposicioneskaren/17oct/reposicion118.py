import math
def cosine(x,n):
	cosx=1
	senal=-1
	for i in range(2,n,2):
		pi=22/7
		y=x*(pi/180)
		cosx=cosx + (senal*(y**i))/math.factorial(i)
		senal=-senal
	return cosx
x=int(input("Escribe valor de x en grados:"))
n=int(input("Escribe numero de terminos:))
pirnt(round(cosin(x,n),2))
