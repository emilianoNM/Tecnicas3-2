import math
def sin(x,n):
	sine=0
	for i in range(n):
		s=(-1)**i
		pi=22/7
		y=x*(pi/180)
		sine=sine + ((y**(2*i+1))/   math.factorial(2*i+1))*s
	return sine
x=int(input("introduce valor de x en grados:"))
n=int(input("escribe numero de termino:))
print(round(sin(x,n),2))

