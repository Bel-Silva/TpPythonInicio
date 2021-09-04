def Potencia (num, elevar):
	cont=1
	result=1
	while cont <= elevar:
		result= result*num
		cont=cont+1
	return result

num1=int(input("Ingrese un número: "))
potencial=int(input("Ingrese la potencia: "))
Resultado= Potencia(num1,potencial)
print(Resultado)