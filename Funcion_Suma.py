cont= 0
def Imprime (a,b):
	print(a*b)

while cont == 0:
	x=input("Ingrese un texto: ")
	y=int(input("Ingrese un número: "))
	Imprime (x,y)
	cont= int(input("Para volver a imprimir ingrese 0, de lo contrario ingrese 1. Respuesta: "))