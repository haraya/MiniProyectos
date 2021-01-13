
def vestimenta(genero):
    vestir = 0
    while (vestir != 1) or (vestir != 2):
        print("\nHa seleccionado la Ropa de " + genero)
        print("\t1) Blusa $35000\n"
              "\t2) Jean $40000")
        vestir = int(input("Seleccione una opcion: "))
        if (vestir == 1) or (vestir == 2):
            return vestir
        else:
            print("Dato erroneo")


def descuento_iva(prenda, impuesto):
    resul = 0
    total = prenda * impuesto
    resul = prenda - total
    return resul


def descuento_especial(monto, des):
    resultado = 0
    respuesta = str(input("¿Tiene un cupon?(Si/No): "))
    if respuesta == 'si' or respuesta == "Si":
        codigo = input("INGRESE EL CUPON :")
        if codigo == "123":
            resultado = monto - (monto * des)
            return resultado
        else:
            print("El cupon es incorrecto")

    elif respuesta == 'no' or respuesta == "No":
        print("Por favor continue con su orden\n")


def despedida():
    print("Gracias por su compra, lo esperamos pronto")


ropa = 0
opcion = 0
iva = 0.19
blusa = 35000
jean = 40000
resultado_iva = 0
resultado_especial = 0
descuento = 0.10


while opcion != 3:
    print("_______SELECCIONE UNA CATEGORÍA_________")
    print("1. Ropa Mujer")
    print("2. Ropa Hombre")
    print("3. Salir")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        ropa = vestimenta("Mujer")

        if ropa == 1:
            print("Ha seleccionado la Blusa")
            resultado_iva = descuento_iva(blusa, iva)
            print("--------------------------------------------------")
            print("El valor de la blusa SIN IVA, es:", resultado_iva)
            print("--------------------------------------------------")
            resultado_especial = descuento_especial(resultado_iva, iva)
            print("__________________________________________________________")
            print("Total Valor del Producto con el 10% Descuento, es: ", resultado_especial)
            print("__________________________________________________________")

        elif ropa == 2:
            print("Ha seleccionado los Jeans")
            resultado_iva = descuento_iva(jean, iva)
            print("--------------------------------------------------")
            print("El valor de la blusa SIN IVA, es:", resultado_iva)
            print("--------------------------------------------------")
            resultado_especial = descuento_especial(resultado_iva, iva)
            print("__________________________________________________________")
            print("Total Valor del Producto con el 10% Descuento, es: ", resultado_especial)
            print("__________________________________________________________")

    elif opcion == 2:
        ropa = vestimenta("Hombre")
        if ropa == 1:
            print("Ha seleccionado la Blusa")
            resultado_iva = descuento_iva(blusa, iva)
            print("--------------------------------------------------")
            print("El valor de la blusa SIN IVA, es:", resultado_iva)
            print("--------------------------------------------------")
            resultado_especial = descuento_especial(resultado_iva, iva)
            print("__________________________________________________________")
            print("Total Valor del Producto con el 10% Descuento, es: ", resultado_especial)
            print("__________________________________________________________")

        elif ropa == 2:
            print("Ha seleccionado los Jeans")
            resultado_iva = descuento_iva(jean, iva)
            print("--------------------------------------------------")
            print("El valor de la blusa SIN IVA, es:", resultado_iva)
            print("--------------------------------------------------")
            resultado_especial = descuento_especial(resultado_iva, iva)
            print("__________________________________________________________")
            print("Total Valor del Producto con el 10% Descuento, es: ", resultado_especial)
            print("__________________________________________________________")

    elif opcion == 3:
        despedida()

    else:
        print("\nDato incorrecto, intentelo de nuevo\n")
