"""
- Pregúntale a la IA 20 preguntas con 4 respuestas que una sea la correcta en un .csv
- El jugador se registra con un nombre, en caso de que el jugador introduzca el mismo nombre el resultado se quedará guardado
- Al final de la partida se mostrará sus aciertos y sus errores
- Al introducir ranking en el nombre se mostrará todos los aciertos y errores de los jugadores registrados
- En caso de que un jugador introduzca el mismo nombre, y ya se haya pasado su partida, se le avisará que se reiniciará su progreso
"""
import csv
import os

archivo_jugadores = "jugadores.csv"


def cargar_jugadores():
    jugadores = {}
    if os.path.exists(archivo_jugadores):
        with open(archivo_jugadores, newline="", encoding="utf-8") as file:
            lector = csv.reader(file)
            for fila in lector:
                nombre, acertadas, equivocadas = fila
                jugadores[nombre] = {"aciertos": int(acertadas), "errores": int(equivocadas)}
    return jugadores


def guardar_jugadores(jugadores):
    with open(archivo_jugadores, "w", newline="", encoding="utf-8") as file:
        escritor = csv.writer(file)
        for nombre, resultados in jugadores.items():
            escritor.writerow([nombre, resultados["aciertos"], resultados["errores"]])


def leer_preguntas():
    preguntas = []
    with open("preguntas.csv", newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for row in lector:
            preguntas.append(row)
    return preguntas


jugadores = cargar_jugadores()
nombre = input("Introduce tu nombre (o 'ranking' para ver todo el ranking): ").strip()

if nombre.lower() == "ranking":
    if jugadores:
        print("\n--- RANKING DE JUGADORES ---")
        for jugador, resultados in jugadores.items():
            print(f"{jugador}: {resultados['aciertos']} aciertos, {resultados['errores']} errores")
    else:
        print("No hay jugadores registrados todavía.")
else:
    if nombre in jugadores:
        print(f"El jugador '{nombre}' ya existe. Se reiniciará su progreso.")

    aciertos = 0
    errores = 0

    preguntas = leer_preguntas()

    for i, pregunta in enumerate(preguntas, 1):
        print(f"\nPregunta {i}: {pregunta['Pregunta']}")
        print(f"A. {pregunta['Opcion_A']}")
        print(f"B. {pregunta['Opcion_B']}")
        print(f"C. {pregunta['Opcion_C']}")
        print(f"D. {pregunta['Opcion_D']}")

        respuesta = input("Tu respuesta (A/B/C/D): ").strip().upper()
        if respuesta == pregunta['Respuesta_Correcta'].upper():
            print("Correcto")
            aciertos += 1
        else:
            print(f"Incorrecto. La respuesta correcta era {pregunta['Respuesta_Correcta'].upper()}")
            errores += 1

    jugadores[nombre] = {"aciertos": aciertos, "errores": errores}
    guardar_jugadores(jugadores)

    print(f"\n--- RESULTADOS DE {nombre} ---")
    print(f"Aciertos: {aciertos}")
    print(f"Errores: {errores}")
