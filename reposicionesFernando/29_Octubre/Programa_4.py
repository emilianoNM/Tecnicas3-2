#En este programa se comparan 2 listas y devulve un verdadero si se tiene al menos un elemento igual

def Comparacion (lista1, lista2):
    for i in lista1:
        for x in lista2:
            if i == x:
                return True
    return False
