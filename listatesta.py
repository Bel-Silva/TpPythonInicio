def h (lista, valor):
	resultado= []
	for elem in lista:
		if elem != valor:
			resultado.append(elem)
	return resultado

a= [1,2,3,4,5,6,5,3]
b= 3
result= h (a,b)
print (result)