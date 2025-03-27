#Programa para Emitir Facturas
print("///Emitir Facturaa///")
cont = 0

while cont != 1:
    producto = input("Ingrese el nombre del producto: ")
    numArt = int(input("Ingrese el total de articulos: "))
    precio = float(input("Ingrese el precio de los articulos: "))
    total = precio*numArt
    suptotal = total+(total*0.15)
    
    if total >= 1000:
        suptotal = total-(total*0.12)
        print("="*20)
        print("        Factura")
        print("Producto.......",producto)
        print("Precio.........",precio)
        print("Articulos......",numArt)
        print("Descuento......","12%")
        print("Impuesto.......","15%")
        print("Subtotal.......",suptotal)
        print("\n")
        opcion = input("Desea emitir otra factura?" )
        if opcion.upper() != "SI":
            print("Gracias por usar este programa")
            cont=1
    else:
        print("="*40)
        print("        Factura")
        print("Producto.......",producto)
        print("Precio.........",precio)
        print("Articulos......",numArt)
        print("Impuesto.......","15%")
        print("Subtotal.......",suptotal)
        print("\n")
        opcion = input("Desea emitir otra factura?" )
        if opcion.upper() != "SI":
            print("Gracias por usar este programa")
            cont = 1
        
        
        
        
