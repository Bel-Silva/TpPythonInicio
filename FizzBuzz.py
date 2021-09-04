
def obtener_FizzBuzz(n):
	if n % 3 ==0 and n % 5 == 0:
		resultado= "FizzBuzz"
		return resultado
	elif n%3 == 0:
		resultado= "Fizz"
		return resultado
	elif n%5 == 0:
		resultado= "Buzz"
		return resultado
	else:
		resultado= "El número no es multiplo de 3 y 5"
		return resultado

num= int(input("Ingrese un número: "))
multiplo= obtener_FizzBuzz(num)
print(multiplo)