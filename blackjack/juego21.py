import random as r

def crearBaraja():
    baraja = []
    valores = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",]
    palos = ["♠️", "♥️","♣️", "♦️"]

    for valor in valores:
        for palo in palos:
            baraja.append(f"{valor} {palo}")
    return baraja

def mezclarBaraja(baraja):
    r.shuffle(baraja)
    return baraja

def repartirBaraja(baraja):
    crupier = [baraja.pop(), baraja.pop()]
    jugador = [baraja.pop(), baraja.pop()]
    return crupier, jugador

def seguirJugando(baraja,jugador,crupier):

    carta = baraja.pop()
    jugador.append(carta)
    print(f"Crupier: {crupier[0]}, 🃏")
    print(f"Jugador: {jugador}")

    return carta,jugador

def valorCarta(carta):
    valor = carta.split()[0]
    if valor in ["J", "Q", "K", "10"]:
        return 10
    elif valor == "As":
        return 11
    else:
        return int(valor)

def valoresCartas(mano):
    valores = [valorCarta(carta) for carta in mano]
    total = sum(valores)

    while total > 21 and 11 in valores:
        valores[valores.index(11)] = 1
        total = sum(valores)
    return total


def comprobarGanador(jugador,crupier,baraja):
    while valoresCartas(crupier) < 17:
        carta = baraja.pop()
        crupier.append(carta)
        print(f"Crupier roba carta: {carta} Total del crupier: {valoresCartas(crupier)}")

    total_jugador = valoresCartas(jugador)
    total_crupier = valoresCartas(crupier)
    print(f"\nJugador: {total_jugador}, Crupier: {total_crupier}")

    if total_jugador > 21:
        print("Te has pasado de 21. Has perdido")
    elif total_crupier > 21:
        print("El crupier se paso de 21. HAS ganado")
    elif total_jugador > total_crupier:
        print("Has ganado")
    elif total_jugador < total_crupier:
        print("Pierdes contra el crupier.")
    else:
        print("Empate.")


def jugar():
    jugar = input("Quieres unirte a la partida (s/n): ")

    if jugar == "s":
        print("Repartiendo cartas...")
        print()
        baraja = crearBaraja()
        baraja_mezclada = mezclarBaraja(baraja)
        jugador, crupier = repartirBaraja(baraja_mezclada)

        print(f"Crupier: {crupier[0]}, 🃏")
        print(f"Jugador: {jugador}")
        print("\n1.Plantar"
              "\n2.Seguir")
        opt = int(input("Elegir opcion: "))
        print()

        salir = True
        while salir:
            if opt != 1:
                seguirJugando(baraja,jugador,crupier)
                print()
                seguir = input("Quieres seguir jugando (s/n): ")
                if seguir == "s":
                    salir
                else:
                    salir = False
                    comprobarGanador(jugador,crupier,baraja_mezclada)
            else:
                salir = False
                comprobarGanador(jugador,crupier,baraja_mezclada)

    else:
        print("Saliendo del juego...")


jugar()

"""
def repartirCarta(mano,carta):
    mano.append(carta)
    if (contarValores(suma) + carta) > 21 and (11 in mano)
    for carta in mano:
    if carta == 11:
    mano[mano.index(carta)] = 1
"""
