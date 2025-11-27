# 2. Llenar una matriz cuadrada (4x4) de números aleatorios del 0 al 9
# mostrar la suma de sus filas y sus columnas.

from utilities import printMatrix
import random as r

matriz = []

for i in range (4):
    matriz.append([])
    for j in range(4):
        matriz[i].append(r.randint(0,9))


printMatrix(matriz)

for f in range(len(matriz)):
    suma = 0
    for c in range(len(matriz)):
        suma += matriz[f][c]

    print(f"La suma de la fila {f} es {suma}")

print()
for c in range(len(matriz)):
    sumaC = 0
    for f in range(len(matriz)):
        sumaC += matriz[f][c]

    print(f"La columna de la fila {c} es {sumaC}")
