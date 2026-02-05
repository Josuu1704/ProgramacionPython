import random
from pprint import pprint

import requests

weather_url = "https://www.eltiempo.es/lluvia"
api_url = "https://pokeapi.co/api/v2/pokemon/"
poke = input("Dime un pokemon -> ")

response = requests.get(api_url+poke)
pokemon = response.json()

movimientos_response = pokemon["moves"]

movimientos = []
for i in range(4):
    movimientos_r = movimientos_response.pop(random.randint(0, len(movimientos_response)))
    pprint(movimientos_r)
