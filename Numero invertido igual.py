#Ejercicio 4 analisis de Numeros
cont = 0

def es_capicua(num):
    numeroStr = str(num)
    numero_invert = numeroStr[::-1]

    return numeroStr == numero_invert
    
while cont != 1:
    print("Este programa Lee un numero de tres cifras y destermia si es igual al reves del numero")
    num = int(input("Ingrese un numero de tres cifras: "))
    
    if 100 <= num <= 999:
        if es_capicua(num):
            print("El número es igual al revés, jejeje.")
        else:
            print("El número no es igual al revés.")
    else:
        print("Por favor, ingrese un número de tres cifras válido.")

    opcion = input("Continuar?...(Si/No): ")
    if opcion != "Si":
        cont = 1

    
        


    
