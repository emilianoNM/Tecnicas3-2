#Este programa utiliza el teorema de pitagorras para dar soluciones


def main():
    
    soluciones = []
    for a in list(range(1,500)):
        for b in list(range(1,500)):
            for c in list(range(1,500)):
                if a**2+b**2 == c**2:
                    soluciones.append(list([a,b,c]))
    print(soluciones)
main()