def palindromo(cadena):
    inicio = 0
    fin = len(cadena) - 1
    while cadena[inicio] == cadena[fin]:
        if inicio >= fin:
            return True
        inicio += 1
        fin -= 1
    return False
texto = input("Ingrese la palabra que desea evaluar: ")
resultado=palindromo(texto)
print(resultado)
