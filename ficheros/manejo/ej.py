"""Vas a crear un programa en Python que gestione archivos y carpetas para una supuesta aplicación de respaldo.
El programa debe hacer lo siguiente:

1. Comprobar si existe un directorio llamado Origen.
2. Si no existe, crearlo y generar dentro varios archivos de texto.
3. Leer el contenido de los archivos usando open().
Comprobar:
4. Si el nombre del archivo termina en .txt usando endswith()
5. Si una palabra clave (por ejemplo "backup") está contenida en el texto usando la cláusula in
6. Copiar archivos válidos a un directorio Respaldo usando shutil.copy
7. Copiar todo el directorio Respaldo a RespaldoTotal usando shutil.copytree
8. Cambia el nombre del archivo que contiene backup a importante.txt
9. Elimina los archivos no válidos con os.unlink"""
import os.path
import shutil

os.chdir("C:\\Users\\Usuario\\Documents")

if not os.path.exists("Respaldo"):
    os.mkdir("Respaldo")

if not os.path.exists("C:\\Users\\Usuario\\Documents\\Origen"):
    os.mkdir("Origen")
    open("Origen\\texto1.txt", "x").write("backup")
    open("Origen\\texto2.txt", "x")
    open("Origen\\texto3.txt", "x")

for archivo in os.listdir("Origen"):
    ruta = os.path.join("Origen", archivo)

    if archivo.endswith(".txt"):
        print(f"{archivo} es valido")

        ruta_respaldo = shutil.copy(ruta, "C:\\Users\\Usuario\\Documents\\Respaldo")

        shutil.copytree("Respaldo", "C:\\Users\\Usuario\\Documents\\RespaldoTotal")
    else:
        print(f"{archivo} No es valido")

for archivo in os.listdir("Origen"):
    ruta = os.path.join("Origen", archivo)


    with open(ruta, "r") as f:
        texto = f.read()
        if "backup" in texto:
            print(f"{archivo} contiene a palabra")
        else:
            print(f"{archivo} No contiene la palabra")
