def ordenamientoBurbuja(nodo):
    unaLista = nodo.getHijos()
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i].peso()>unaLista[i+1].peso():
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp
	return unaLista