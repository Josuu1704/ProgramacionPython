"""
5. Programa un juego de búsqueda de un tesoro. Contaremos con una matriz de 4x5, tendremos un tesoro y una mina. El juego termina cuando
pisas la mina (pierdes) o cuando encuentras el tesoro (ganas). El menú de juego tendrá el siguiente aspecto:

¡Busca el tesoro!
3|
2|
1|
0|
  ----------
   0 1 2 3 4

Coordenada x: (input del usuario, p.e. 3)
Coordenada y: (input, p.e. 1)

3|
2|
1|       X
0|
  ----------
   0 1 2 3 4

Coordenada x: (input del usuario, p.e. 2)
Coordenada y: (input, p.e. 0)

3|
2|
1|       X
0| X
  ----------
   0 1 2 3 4

Coordenada x: (input del usuario, p.e. 2)
Coordenada y: (input, p.e. 2)

¡Enhorabuena, has encontrado el tesoro!
3|
2|     €
1|       X
0| X   *        <-- Aquí estaba la mina. Programar también cuando pierdes.
  ----------
   0 1 2 3 4


"""
import copy
import random as r


def dibujarMapa(m):
    x = 3
    for i in range(len(m)-1,-1,-1):
        print(f"{x}: {m[i]}")
        x -= 1
    print("     0    1    2    3    4")


def dibujarMapaVacio(m):
    x = 3
    for i in range(len(m)-1,-1,-1):
        print(f"{x}: {m[i]}")
        x -= 1
    print("    0,  1,  2,  3,  4")

def generarItems(m):
    mina = "💣"
    tesoro = "💰"
    coordsMina = (r.randint(0,4),r.randint(0,3))
    coordsTesoro = coordsMina
    while coordsMina == coordsTesoro:
        coordsTesoro = (r.randint(0,4), r.randint(0,3))
    m[coordsMina[1]][coordsMina[0]] = mina
    m[coordsTesoro[1]][coordsTesoro[0]] = tesoro
    return coordsMina, coordsTesoro

def cavar(m, m2):
    print("Introduce las coordenadas que quieras cavar:")
    coords = int(input("X: ")), int(input("Y: "))
    m[coords[1]][coords[0]] = "⛏"
    m2[coords[1]][coords[0]] = "⛏"
    return coords

mapa =[["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
mapaVacio = copy.deepcopy(mapa)

dibujarMapa(mapa)
coordsMina, coordsTesoro = generarItems(mapa)

fin = False
print(f"coordsMina:  {coordsMina}")
print(f"coordsTesoro:  {coordsTesoro}")

while not fin:
    coordsCavar = cavar(mapaVacio, mapa)
    if coordsCavar == coordsTesoro:
        print("has ganado")
        dibujarMapa(mapa)
        fin = True
    elif coordsCavar == coordsMina:
        print("Has perdido")
        dibujarMapa(mapa)
        fin = True
    else:
        dibujarMapa(mapaVacio)


