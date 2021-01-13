from datetime import datetime
import operator

# Diccionario Original
diccionario = {"Carmenza": "2003/12/21", "Juliana": "1991/11/11", "Patricia": "1991/11/11",  "Mariana": "2003/4/14",
               "JeanC": "2001/9/11",     "LuisE": "1991/11/11",   "Vanessa": "2003/1/8",     "Joiber": "2001/9/4",
               "DanielE": "2003/6/20",   "Lothar": "2002/7/16",   "Valentina": "2003/12/21", "LauraV": "2001/8/31",
               "JeisonD": "2003/6/11",   "GabrielF": "2002/6/26", "Nicholas": "1993/11/19",  "Hector": "1991/11/22",
               "Roiver": "2002/10/14",   "Oliver": "2002/10/11",  "Jader": "2001/12/25",     "JuanDav": "2002/9/12",
               "Jeynner": "2001/3/13",   "Gabriela": "2001/11/20", "AndresJ": "2002/4/4",    "JuanDieg": "2002/10/1"}


# Extraemos del diccionario las personas, las fechas y las guardamos en una lista cada uno
lista_personas = list(diccionario.keys())
lista_fecha = list(diccionario.values())

# Ciclo para guardar la fecha del diccionario en formato fecha
fecha = []
fechaux = []
for f in lista_fecha:
    dato = datetime.strptime(f, '%Y/%m/%d')
    fecha.append(dato)
    fechaux.append(str(dato))

# Ciclo para guardar los meses de cada persona del diccionario
lista_meses = []
for m in fecha:
    mes = m.strftime('%m')
    lista_meses.append(int(mes))


# Creamos una lista con los meses en palabras y otra con los meses en numeros
mes_palabra = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
               "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
mes_numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


# Creamos un diccionario de los meses con los numeros respectivos
meses_diccionario = dict(zip(mes_palabra, mes_numero))


# Creamos un diccionario donde guardaremos las personas y sus respectivos meses
diccionario_personas_mes = dict(zip(lista_personas, lista_meses))

# Creamos un diccionario donde guardaremos las personas y sus respectivas fechas
diccionario_personas_fecha = dict(zip(lista_personas, fechaux))

# Creamos un nuevo diccionario donde esta ordenado por la fecha de nacimiento
diccionario_ordenado = dict(sorted(diccionario_personas_fecha.items(), key=operator.itemgetter(1)))

# Convertimos el diccionario ordenado en una lista
lista_ordenada = list(diccionario_ordenado)

nuevo = dict(zip(lista_personas, lista_fecha))
opcion = 0
# Menu del Programa
while opcion != 6:
    print("1.Personas cumplen en un mes en específico\n"
          "2.Cantidad de personas que cumplen en cada mes\n"
          "3.Personas que cumplen en cada mes\n"
          "4.Persona con mayor edad\n"
          "5.Persona con menor edad\n"
          "6.Salir")
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        usuario_mes = str(input("Ingrese un mes: "))

        print("\nPersonas que cumplen en:", usuario_mes)
        for clave, valor in meses_diccionario.items():
            for persona, mes in diccionario_personas_mes.items():

                if (usuario_mes == clave) and (valor == mes):
                    for p, f in nuevo.items():
                        if p == persona:
                            print(persona, f)
        print()

    elif opcion == 2:
        personas = []
        numeros = []
        numero = 0
        print(" ")
        for clave, valor in meses_diccionario.items():
            for persona, mes in diccionario_personas_mes.items():

                if valor == mes:
                    personas.append(persona)
                    numero = numero + personas.count(persona)
            numeros.append(numero)
            numero = 0

        cumple_personas_mes = dict(zip(mes_palabra, numeros))

        for m, nu in cumple_personas_mes.items():
            print(f"Personas que cumplen en {m}: {nu}")
        print()

    elif opcion == 3:
        person = []
        numeros = []
        aux = " "

        print("")
        for clave, valor in meses_diccionario.items():
            for persona, mes in diccionario_personas_mes.items():

                if valor == mes:
                    person.append(persona)
                    aux = aux + persona + ", "
            numeros.append(aux)
            aux = " "

        cumple_personas_mes = dict(zip(mes_palabra, numeros))

        for m, nu in cumple_personas_mes.items():
            print(f"En {m} cumple:{nu}")

        print()

    elif opcion == 4:
        print(lista_ordenada[0], "es la persona de Mayor edad\n")

    elif opcion == 5:
        print(lista_ordenada[-1], "es la persona de Menor edad\n")

    elif opcion == 6:
        print("Adios!")
