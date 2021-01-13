def maquina_bebidas(nombre, cantidad):
    stock = 0
    monto = 0
    print(f"Ha seleccionado {nombre}")
    if cantidad <= 0:
        print("Productos agotados")
    else:
        print("Total a pagar: ", 10)

        while monto < 10:
            monedas = int(input("Deposite moneda (acepta $1 $2 $5 $10): "))
            monto = monto + monedas
            print("Total depositado: $", monto)

            if monto == 10:
                print("Recoja su producto")
        stock = cantidad - 1
        print("Productos en stock", stock)

        monto = 0
    cantidad -= 1
    return cantidad


cocacola = 5
fanta = 5
manzanita = 5
sprite = 5
cocacolalight = 5

bebida = 0


while bebida != 5:
    print("\nMenu refrescos\n"
          "1.Coca cola\n"
          "2.Fanta\n"
          "3.Manzanita\n"
          "4.Sprite\n"
          "5.Coca cola light")
    bebida = int(input("Ingrese una opcion: "))

    if bebida == 1:
        cocacola = maquina_bebidas("Coca Cola", cocacola)

    elif bebida == 2:
        fanta = maquina_bebidas("Fanta", fanta)

    elif bebida == 3:
        manzanita = maquina_bebidas("Manzanita", manzanita)

    elif bebida == 4:
        sprite = maquina_bebidas("Sprite", sprite)

    elif bebida == 5:
        cocacolalight = maquina_bebidas("Coca Cola light", cocacolalight)

    else:
        print("Numero incorrecto, intente de nuevo\n")
