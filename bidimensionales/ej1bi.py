"""
1. Dibujar una matriz cuadrada con el tamaño definido por el usuario y que pinte de unos la diagonal inversa.
"""

from utilities import printMatrix

matriz = []

tamaño = int(input("Introudce el tamaño de la matriz: "))

for i in range(tamaño):
    matriz.append([])
    for j in range(tamaño):
        matriz[i].append(0)

for i in range(4):
    matriz[i][4 - 1 - i] = 1

printMatrix(matriz)