import shutil, os

#os.chdir("C:\\Users\\Usuario\\Desktop")
#print(os.listdir())
#print(os.path.exists("ejemplo.txt"))

#if "ejemplo.txt" in os.listdir():
#    print("Si que esta")

#shutil.copy("ejemplo.txt", "C:\\Users\\Usuario\\Documents\\nombrenuevo.txt")
#shutil.copytree("Vacia", "C:"\\Users\\Usuario\\Documents\\

#Fija un sitio chdir
#Crea una carpeta os.mkdir()
#Crea un file dento con oper()
#Copiala en el escritorio con lo que tiene dentro

os.chdir("C:\\Users\\Usuario\\Documents\\ManejoFicherps")
#os.mkdir("ParaCopiar")

if not os.path.exists("nuevo.txt/ficheros.txt"):

    open("nuevo.txt", "x")

#shutil.copytree("ParaCopiar", "C:\\Users\\Usuario\\Desktop\\Copiada")

#os.unlink() #Borra los ficheros
#os.rmdir()#Borra los directorios
#shutil.rmtree()#Borra la carpeta recursivamente
#shutil.move("nuevo.txt", "C:\\Users\\Usuario\\Desktop\\")

#"".endswith()
