#Importe a pagar por vehiculo
vehiculo=input("Ingrese el tipo de vehiculo para calcular el importe a pagar: ")

if vehiculo=="Bisicleta" or vehiculo=="bisicleta":
    print("El importe: 100 cordobas")
    
elif vehiculo=="Moto" or vehiculo=="carro":
    km = int(input("Ingrese los kilometros recorridos: "))
    Importe = km*30
    print ("El importe: ", Importe,"C$")
    
elif vehiculo=="camion":
    km = int(input("Ingrese los kilometros recorridos: "))
    Tn = float(input("Ingrese las toneladas totales:"))
    Importe = (km*30)+(Tn*25)
    print ("Importe Total: ",Importe,"C$")

else:
    print("El tipo de vehiculo no exite o esta mal escrito, intentelo de nuevo ;)")
    
