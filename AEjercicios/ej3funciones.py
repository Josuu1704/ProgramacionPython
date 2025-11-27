import random

nombres = []
continuar = True
intentos = 0

def darPista(nombre, nombreDesordenado):
    letra = nombreDesordenado.pop()
    print("_"*posicion+letra+"_"*(len(nombre)- posicion -1))




for i in range(5):
    nombre = input(f"Introduce el nombre {i+1}: ")
    nombres.append(nombre)

print(nombres)

nombre_aleatorio = nombres[random.randint(0, (len(nombres)-1))]

letras = [l for l in nombre_aleatorio ]
random.shuffle(letras)
#letra = []
#for l in letras:
#   letras.append(l)

print(nombre_aleatorio)

while intentos < 3:
    seleccion = input("Introduce tu nombre elegido: \n")
    if seleccion != nombre_aleatorio:
        print("INCORRECTO. INTENTALO DE NUEVO")
        intentos+= 1
        darPista(letras)

    elif seleccion == nombre_aleatorio:
        continuar = True
        print("CORRECTO. HAS GANADO")

else:
    print("HAS PERDIDO. ")

