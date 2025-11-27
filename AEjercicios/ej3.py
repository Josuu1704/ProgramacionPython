#Genera un programa que permita al usuario introducir una serie de nombres.Minimo 5 nombres
# Una vez terminada la introduccion, el programa seleccionara aleatoriamente un nombre
# Ahora, el usuario-jugador tendra que introducir nombres hasta adivinar el nombre elegido por la maquina.
#Contara con 3 intentos
#Bonus: en cada intento, la mquina nos dará una pista, una letra de una posicion del nombre
#Ej: "La tercera letra es una i

import random
import random as r

nombres = []
intentos = 0
terminar = True

for i in range(5):
    nombre = input(f"Introduce el nombre {i+1}: ")
    nombres.append(nombre)

print(nombres)

nombre_aleatorio = nombres[r.randint(0, (len(nombres)-1))]
print(nombre_aleatorio)

while intentos < 3:
    seleccion = input("Introduce tu nombre elegido: \n")
    if seleccion != nombre_aleatorio:
        print("INCORRECTO. INTENTALO DE NUEVO")
        intentos+= 1
        letra = random.choice(nombre_aleatorio)
        print(f"Contiene la letra {letra}\n")

    elif seleccion == nombre_aleatorio:
        print("CORRECTO. HAS GANADO")

else:
    print("HAS PERDIDO. ")




