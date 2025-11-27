class Perro:
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __init__(self):
        return f"Soy {self.nombre}, tenoo {self.edad}"

    def comer(self, comidaEnGramos):
        self.peso +=comidaEnGramos
        print(f"{self.nombre}, comio {comidaEnGramos} y pesa {self.peso}")

    def cagar(self, cacaEnGramos):
        self.peso -= cacaEnGramos
        print(f"{self.nombre} ha cagado {cacaEnGramos} y pesa {self.peso}")