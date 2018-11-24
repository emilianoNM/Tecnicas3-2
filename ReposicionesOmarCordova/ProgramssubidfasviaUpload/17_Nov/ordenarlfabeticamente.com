palabra = raw_input("\n..:Ordenar Alfabeticamente:..\n>Dame la palabra (solo minusculas): ")
convertido = list(palabra)
convertido = convertido.sort()
print convertido