#Ejemplo de menu de opciones
print("Seleccione al accion a realizar:")
print("1.Abrir archivo")
print("2.Guardar archivo")
print("3.Salir del programa")

opcion = input()
if opcion == "1" or opcion == "Abrir archivo":
    print("Archivo abierto con exito")
elif opcion == "2" or opcion == "Guardar archivo":
    print("Archivo guardado con exito")
elif opcion == "3" or opcion == "Salir del programa":
    print("Saliendo...")
else:
    print("Obcion no validad, intentelo de nuevo")
