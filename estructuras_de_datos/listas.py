from estructuras_de_datos.perro import Perro

tupla = (1,3,5)
lista = []
diccionario = {}

perrito = Perro("Tomas", 4)
print(perrito)
print(perrito.nombre)
print(perrito.edad)
print(perrito.raza)

perrito.comer(200)
perrito.cagar(300)

perrito.peso = 2000