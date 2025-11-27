# 3. Comprobar si una matriz dada es un cuadrado mágico.
# cuadradoMágico = [[16,3,2,13], [5,10,11,8], [9,6,7,12], [4,15,14,1]]
from utilities import printMatrix

m = [[16,3,2,13], [5,10,11,8], [9,6,7,12], [4,15,14,1]]
esMagico = True
filaMagica = sum(m[0])
sumaF = 0


for f in m:
    if sum(f) != filaMagica:
        esMagico = False

for c in range(len(m)):
    sumaC = 0
    for f in range(len(m)):
        sumaC += m[f][c]
    if sumaC != filaMagica:
        esMagico = False

suma_diag1 = 0
for f in range(len(m)):
    suma_diag1 += m[f][f]

if suma_diag1 != filaMagica:
    esMagico = False

suma_diag2 = 0
for f in range(len(m)):
    suma_diag2 += m[f][len(m) - 1 - f]

if suma_diag2 != filaMagica:
    es_magico = False


printMatrix(m)

if esMagico:
    print("Es un cuadrado mágico")
else:
    print("No es un cuadrado mágico")