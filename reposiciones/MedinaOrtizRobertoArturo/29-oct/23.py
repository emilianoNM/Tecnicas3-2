def encontrar(p,a):
	t=len(a)-1
	for i in a:
		print i
		if i in p:
			
			print a.index(i)
			if a.index(i)==t:	
				print 'True'
			pass
		else:
			print 'False'
			break





p=['0','1','2','3','4','5','6','7','8','9']
a=list(raw_input('Ingresa la cadena: '))
print a
encontrar(p,a)