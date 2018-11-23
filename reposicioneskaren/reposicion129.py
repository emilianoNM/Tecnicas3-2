d={'A':,'B':2,'C':3}
key=raw_input("escribe contrasena a evaluar")
if key in d.keys():
	print("la contrasena es:")
	print(d[key])
else:
	print("la llave no esta")
