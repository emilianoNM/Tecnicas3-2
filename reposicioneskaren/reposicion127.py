def modificar(cade):
	final=""
	for i in range(len(cade)):
		if i%2==0:
			final=final+cade[i]
	return final
cade=raw_input("escribir palabra:")
print("modificada")
print(modificar(cade))
