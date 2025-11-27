#Un programa que reciba una cantidad de n de minutos y muestra las horas y minutos que son

minutos = int(input("Introduce los minuts que quieras: "))
horas = minutos // 60

if minutos % horas == 0:
    print(f"Hay {horas} horas")
else:
    print(f"Son {horas} hora y {minutos} minutos")