#Oferta de supermercado
print("//////////Registro//////////")
cont = 0

while cont != 1:
    numDocen = int(input("Ingrese el numero de docenas: "))
    precProduc = float(input("Ingrese el precio del articul0: "))
    numProduc = numDocen*12
    total = numProduc*precProduc
               
    if numProduc > 3:
        descuento = total*0.15
        uniExtr = numDocen-3
        subtotal = total-descuento
        print("=="*30)
        print("SubTotales")
        print("=="*30)
        print("1.Monto de la compra...       ",total)
        print("2.Monto del Descuento...      ",descuento)
        print("3.Monto a pagar...            ",subtotal)
        print("4.Unidades de obsequio...     ",uniExtr)
        print("=="*30)
    else:
        descuento = total*0.10
        uniExtr = 0
        subtotal = total-descuento
        print("=="*30)
        print("SubTotales")
        print("=="*30)
        print("1.Monto de la compra...       ",total)
        print("2.Monto del Descuento...      ",descuento)
        print("3.Monto a pagar...            ",subtotal)
        print("4.Unidades de obsequio...     ",uniExtr)
        print("=="*30)
        
    opcion = input("Continuar..(Si/No): ")
    if opcion.upper() != "SI":
        cont = 1
    
        
    
        
        
        
