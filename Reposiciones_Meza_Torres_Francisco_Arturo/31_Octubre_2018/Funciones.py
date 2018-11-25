#!/usr/bin/env python
def multiplo7(n):
	if n%7==0:
		return True
	else:
		return False
for i in range(1,1001):
	if multiplo7(i)==1:
		print i

def multiplo7(n):
return n%7==0