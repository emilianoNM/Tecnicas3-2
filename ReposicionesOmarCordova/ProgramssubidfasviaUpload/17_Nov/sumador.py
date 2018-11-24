def sumandoCifras():
    dato = []
    tmp = int(raw_input("\n..:Suma de Numeros:..\n> Dame la cantidad de numero a sumar: "))
    for i in range(tmp):
        n = int(raw_input("> El numero [{}] es: ".format(i+1)))
        dato.append(n)
    res = sum(dato)
    print "> Resultado de la suma es: {}".format(res)
sumandoCifras()