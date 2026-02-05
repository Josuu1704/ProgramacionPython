import random
import requests
from pprint import pprint

API_URL = "https://pokeapi.co/api/v2/pokemon/"


class Pokemon:
    def __init__(self, nombre, tipos, movimientos, stats):
        self.nombre = nombre
        self.tipos = tipos
        self.movimientos = movimientos
        self.stats = stats


def obtener_pokemon(nombre_pokemon):
    response = requests.get(API_URL + nombre_pokemon.lower())
    pokemon = response.json()

    nombre = pokemon["name"]

    tipos = []
    for t in pokemon["types"]:
        tipos.append(t["type"]["name"])

    stats = {}
    for stat in pokemon["stats"]:
        stats[stat["stat"]["name"]] = stat["base_stat"]

    movimientos_api = pokemon["moves"]
    movimientos = []

    contador = 0
    while contador < 4:
        indice = random.randint(0, len(movimientos_api) - 1)
        movimiento = movimientos_api.pop(indice)

        move_url = movimiento["move"]["url"]
        move_data = requests.get(move_url).json()

        movimientos.append({
            "move_name": move_data["name"],
            "move_power": move_data["power"],
            "move_pp": move_data["pp"]
        })

        contador += 1

    return Pokemon(nombre, tipos, movimientos, stats)



poke_1 = input("Ingresa el primer Pokémon: ")
poke_2 = input("Ingresa el segundo Pokémon: ")

pokemon1 = obtener_pokemon(poke_1)
pokemon2 = obtener_pokemon(poke_2)

print("\nPOKÉMON 1")
pprint(vars(pokemon1))

print("\nPOKÉMON 2")
pprint(vars(pokemon2)) 
