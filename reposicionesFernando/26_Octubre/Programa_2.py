#Este programa calcula el area de un rectangulo por medio de clases

class Rectangulo():
    def __init__(self,Ancho,Largo):
        self.Ancho=Ancho
        self.Largo=Largo
    def area(self):
        return self.Ancho*self.Largo
a=int(input("Introduzca el Largo del Rectangulo: "))
b=int(input("Introduzca el Ancho del Rectangulo: "))
obj=Rectangulo(a,b)
print("Area del Rectangulo:",obj.area())
 
print()