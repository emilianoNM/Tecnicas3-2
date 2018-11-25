#!/usr/bin/env python

def fib(n): # N´umeros de Fibonacci
	a,b=0,1
	r=[] # r tendr´a el resultado
	while b<n:
		r.append(b)
		a,b=b,a+b
	return r
print fib(10)