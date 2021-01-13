
i = 1
subsidio = 877.803
lista = []

print("Registro de personas")
cantidad = int(input("Digite la cantidad de personas a ingresar: "))

while i <= cantidad:
    print("Persona#", i)
    nombre = input("Digite su nombre completo: ")
    lista.append("Nombre: " + nombre)

    print("Digite su sexo")
    print("1.Masculino\n"
          "2.Femenino")
    sexo = int(input("Sexo: "))
    if sexo == 1:
        lista.append("Sexo: Masculino")
    elif sexo == 2:
        lista.append("Sexo: Femenino")

    edad = int(input("Digite su edad: "))
    lista.append("Edad: " + str(edad))

    print("Digite su nivel de estudio")
    print("1.Bachiller\n"
          "2.Pregrado\n"
          "3.Maestria\n"
          "4.Doctorado")
    nivel: int = int(input("Nivel de estudio: "))
    if nivel == 1:
        lista.append("Nivel de estudio: Bachillerato")
    elif nivel == 2:
        lista.append("Nivel de estudio: Pregrado")
    elif nivel == 3:
        lista.append("Nivel de estudio: Maestria")
    elif nivel == 4:
        lista.append("Nivel de estudio: Doctorado")

    hijos = int(input("Digite la cantidad de hijos que tiene: "))
    lista.append("Cantidad de hijos: " + str(hijos))

    print("¿Esta trabajando?")
    trabajo = int(input("1.Si\n"
                        "2.No\n"))
    print("------------------------------------------------------\n")

    # trabaja o no
    if trabajo == 1:
        trabajo1 = "Si esta trabajando"
        lista.append("Estado actual: " + trabajo1)
    elif trabajo == 2:
        trabajo1 = "No esta trabajando"
        lista.append("Estado actual: " + trabajo1)
    # ------------------------------------------------

    # nivel bachiller
    if nivel == 1 and trabajo == 1:
        subtotal = (subsidio * 0.20) * hijos
        lista.append("El monto es: " + str(subtotal))

    elif nivel == 1 and trabajo == 2:
        flojo = (subsidio * 0.25)
        aaaa = (subsidio * 0.20) * hijos
        subtotal = aaaa + flojo
        lista.append("El monto es: " + str(subtotal))

    # -----------------------------------------------
    # nivel pregrado
    elif nivel == 2 and trabajo == 1:
        subtotal = (subsidio * 0.30) * hijos
        lista.append("El monto es: " + str(subtotal))

    elif nivel == 2 and trabajo == 2:
        flojo = (subsidio * 0.25)
        aaaa = (subsidio * 0.30) * hijos
        subtotal = aaaa + flojo
        lista.append("El monto es: " + str(subtotal))

    # -------------------------------------------------------
    # nivel maestria
    elif nivel == 3 and trabajo == 1:
        subtotal = (subsidio * 0.40) * hijos
        lista.append("El monto es: " + str(subtotal))

    elif nivel == 3 and trabajo == 2:
        flojo = (subsidio * 0.25)
        aaaa = (subsidio * 0.40) * hijos
        subtotal = aaaa + flojo
        lista.append("El monto es: " + str(subtotal))

    # ----------------------------------------------------------
    # nivel doctor
    elif nivel == 4 and trabajo == 1:
        subtotal = (subsidio * 0.50) * hijos
        lista.append("El monto es: " + str(subtotal))

    elif nivel == 4 and trabajo == 2:
        flojo = (subsidio * 0.25)
        aaaa = (subsidio * 0.50) * hijos
        subtotal = aaaa + flojo
        lista.append("El monto es: " + str(subtotal))

    i += 1

for p in lista:
    print(p)
