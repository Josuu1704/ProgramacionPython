"""
Crear, si no existe ya, un archivo csv de algo que os interese.
Gestionar la creación de nuevas tuplas.
Acceder a un dato de una tupla.
etapas-camino.csv
Partida:
Llegada:
km:
hayPublico:
lubian;a gudiña;23.7;True
a gudiña;laza;34.0;False
lubian;a gudiña;23.7;True
a gudiña;laza;34.0;False
cadena= "Hola, buenas, qué tal?"
arrayDeElementosSeparadosPorElArgumento = cadena.split(",")
print(array)
["Hola", " buenas", "qué tal?"]
Nuevo script
A partir del csv anterior, crea un csv nuevo con los gustos del usuario y la información que él decida
guardar.
etapas-camino.csv -> etapas-favoritas.csv
Solo las etapas que me interesan, con sólo los datos que me interesan
Llegada
km
a gudiña;23,7
laza;34
"""
import os

def addRowToCSV(tupla, rutaFichero):
    info = ""
    for i in range(len(tupla) - 1):
        info += f"{tupla[i]},"
    info += f"{tupla[-1]}\n"
    with open(rutaFichero, "a") as f:
        f.write(info)

rutaFichero = "peliculas.csv"

if(os.path.exists("peliculas.csv")):
    print("Ya existe")
else:
    open("peliculas.csv", "x")

addRowToCSV(["Pelicula", "Categorñia" ,"Visto"], rutaFichero)
addRowToCSV(["Avengers", "Accion" ,True], rutaFichero)
addRowToCSV(["Avatar", "Accion" ,False], rutaFichero)
addRowToCSV(["Minecraft", "Accion" ,True], rutaFichero)