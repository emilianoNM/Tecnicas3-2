s1=raw_input("escribe la primer palabra")
s2=raw_input("escribe la segunda palabra")
a=list(set(s1)-set(s2))
print("las letras son:")
for i in a:
	print(i)
