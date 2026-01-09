import os


def addRowToCSV(tupla, rutaFichero):
    info = ""
    for i in range(len(tupla) - 1):
        info += f"{tupla[i]},"
    info += f"{tupla[-1]}\n"
    with open(rutaFichero, "a") as f:
        f.write(info)

def createRow():
    partida = input("Introduce la etapa de partida")
    llegada = input("Introduce la etapa de llegada")
    try:
        km = float(input("Introduce los km de la etapa"))
    except ValueError:
        km = float(input("Introduce un numero decimal"))
    pregunta = input("¿Hay hostal público?")
    if pregunta == "s":
        hayPublico = True
    else:
        hayPublico = False
    return [partida, llegada, km, hayPublico]

def acceder_datos(rutaFichero):
    with open(rutaFichero, "r") as f:
        linea = f.readlines()

        for i in range(1, len(linea)):
            datos = linea[i].split(",")

            km = float(datos[2])
            if km > 30:
                partida = datos[0]
                llegada = datos[1]
                print(f"Partida: {partida} - Llegada: {llegada} ({km} km)")

rutaFichero = "etapas-camino.csv"

if(os.path.exists("etapas-camino.csv")):
    print("Existe")
else:
    with open(rutaFichero, "w") as f:
        f.write("Partida, Llegada, KM, Hostal público\n")


def menu():
    salir = False
    while not salir:
        print("\n--- MENÚ ---")
        print("1. Añadir etapa")
        print("2. Acceder a datos")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            addRowToCSV(createRow(), rutaFichero)
        elif opcion == "2":
            acceder_datos(rutaFichero)
        elif opcion == "3":
            print("Saliendo del programa")
            salir = True
        else:
            print("Opción no válida. Intenta de nuevo.")

menu()