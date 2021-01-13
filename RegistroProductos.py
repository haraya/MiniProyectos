

lista_id = []
lista_nombre = []
lista_preciocosto = []
lista_precioventa = []

precio = 0
opcion = 0
ganancias = 0
contador = 0
total_ventas = 0
pedir = 1
calculo_iva = 0

while opcion <= 6:
    print("\nMenu de opciones: \n"
          "1.Agregar productos\n"
          "2.Venta de producto\n"
          "3.Ver Ganancias\n"
          "4.Calcular IVA\n"
          "5.Modificar producto\n"
          "6.Elimnar producto")
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        print("\nAgregar Producto")
        ski = str(input("ID del producto: "))
        nombre = str(input("Nombre del producto: "))
        preciocosto = int(input("Precio costo del producto: "))
        precioventa = int(input("Precio venta del producto: "))

        ganancias = ganancias + (precioventa - preciocosto)

        lista_id.append(ski)
        lista_nombre.append(nombre)
        lista_preciocosto.append(preciocosto)
        lista_precioventa.append(precioventa)

    elif opcion == 2:
        print("\nVenta de productos")
        for dele in range(len(lista_id)):
            print(dele + 1, lista_nombre[dele], "costo: ", lista_precioventa[dele])

        numero = int(input("Digite el numero del producto: "))
        print("Ha seleccionado ", lista_nombre[numero-1], "y el precio es", lista_precioventa[numero-1])
        cantidad = int(input("Digite la cantidad del producto: "))
        precio = cantidad * lista_precioventa[numero-1]
        print("El precio a pagar es: ", precio)
        total_ventas += precio

    elif opcion == 3:
        print("\nVer Ganancias")
        print("Las ganancias son: ", ganancias)

    elif opcion == 4:
        print("\nCalcular IVA")
        calculo_iva = (total_ventas * 0.12)
        print("El monto a pagar del IVA es de:", calculo_iva)

    elif opcion == 5:
        print("\nModificar producto")

        for dele in range(len(lista_id)):
            print(dele + 1, lista_nombre[dele])

        numero = int(input("Digite el numero del producto a modificar: "))
        print("Ha seleccionado ", lista_nombre[numero-1])
        print("1. ID\n"
              "2. Nombre\n"
              "3. Precio compra\n"
              "4. Precio venta")
        modificar = int(input("Que desea modificar:"))
        if modificar == 1:
            idaux = str(input("Ingrese el nuevo ID: "))
            lista_id[numero-1] = idaux
            print("Se ha modificado con exito")

        elif modificar == 2:
            nombreaux = str(input("Ingrese el nuevo nombre: "))
            lista_nombre[numero-1] = nombreaux
            print("Se ha modificado con exito")

        elif modificar == 3:
            pcaux = int(input("Ingrese el nuevo precio compra: "))
            lista_preciocosto[numero-1] = pcaux
            print("Se ha modificado con exito")

        elif modificar == 4:
            pvaux = int(input("Ingrese el nuevo precio venta: "))
            lista_precioventa[numero-1] = pvaux
            print("Se ha modificado con exito")

    elif opcion == 6:
        print("\nEliminar producto")
        for dele in range(len(lista_id)):
            print(dele + 1, lista_nombre[dele])

        numero = int(input("Digite el numero del producto a eliminar: "))
        lista_id.remove(lista_id[numero-1])
        lista_nombre.remove(lista_nombre[numero - 1])
        lista_preciocosto.remove(lista_preciocosto[numero - 1])
        lista_precioventa.remove(lista_precioventa[numero - 1])

        print("Se ha eliminado el producto con exito")

    else:
        print("El dato ingresado es incorrecto, intentelo de nuevo")
