def norepetido(repetidas,a):
	for i in a:
		if i in repetidas:
			pass
		else: 
			print 'La letra ',i,' es la primera no reptida' 
			break

a=list(raw_input('Ingresa una cadena: '))
b=sorted(a)
repetidas=[]
for i in range(1,len(a)-1):
	if b[i]==b[i+1]:
		repetidas.append(b[i])
print repetidas
norepetido(repetidas,a)
