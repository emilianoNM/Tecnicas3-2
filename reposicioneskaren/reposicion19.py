terminos=10
n1=0
n2=1
cont=0

if terminos<=0:
	print("introduce uno positivo")
elif terminos==1:
	print("Secuencia de Fibonacci",terminos,":")
	print(n1)
else:
	print("Secuenia de Fibonacci",terminos,":")
	while cont<terminos:
		print(n1,terminos,',')
		nth=n1+n2
		n1=n2
		n2=nth
		cont+=1
