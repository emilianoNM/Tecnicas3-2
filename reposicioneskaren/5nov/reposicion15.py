import turtle
def cuadrado:
	turtle.pen()
	turtle.forward(100)
	turtle.left(90)
	turtle.forward(100)
	turtle.left(90)
	turtle.forward(100)
	turtle.left(90)
	turtle.forward(100)
def triangulo:
	turtle.pen()
	turtle.forward(100)
	turtle.left(120)
	turtleforward(100)
	turtle.left(120)
	turtle.forward(100)
opciones=['cuadrado','triangulo']
print('opciones:',opciones)
eleccion=input("que figura quiere dibujar:")
if eleccion="cuadrado":
	cuadrado()
else:
	triangulo()
