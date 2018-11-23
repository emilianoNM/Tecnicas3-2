def anagrama(a,b):
	if len(a)==len(b):
		for i in range(1,len(a)-1):
			if a[i]!=b[i]:
				print 'No es un anagrama'
				break
		print 'Es un anagrama'		


a=list(raw_input('Ingresa palabra 1: '))
b=list(raw_input('Ingresa palabra 2: '))

a.sort()
b.sort()

anagrama(a,b)