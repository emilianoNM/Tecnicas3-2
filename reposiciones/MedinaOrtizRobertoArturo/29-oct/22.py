def reverse(lis):
    if len(lis)==1:
        return lis
    else:

        return list(lis[-1])+reverse(lis[:-1])

a=list(raw_input('Ingrese la cadena: '))
ai=reverse(a)
print ai