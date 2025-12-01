def menu_principal_general():
    print("\n=== Menú principal ===")
    print("1. Añadir diccionario")
    print("2. Eliminar diccionario")
    print("3. Ver diccionario general")
    print("4. Salir")


def menu_diccionario_anidado():
    print("\n--- Menú de diccionario interno ---")
    print("1. Añadir clave")
    print("2. Eliminar clave")
    print("3. Mostrar diccionario")
    print("4. Finalizar y guardar")


def elegir_tipo_valor():
    print("\nTipos de valor disponibles:")
    print("1. String")
    print("2. Int")
    print("3. Float")
    print("4. Lista")
    print("5. Diccionario")
    tipo = input("Seleccione tipo de valor:\n>> ")
    return tipo


def pedir_valor(tipo):
    if tipo == "1":  # String
        return input("Introduce un valor (string):\n>> ")

    elif tipo == "2":  # Int
        return int(input("Introduce un valor (int):\n>> "))

    elif tipo == "3":  # Float
        return float(input("Introduce un valor (float):\n>> "))

    elif tipo == "4":  # Lista
        lista = []
        cont = True
        while cont:
            valor = input("Introduce un elemento para la lista ('n' para terminar):\n>> ")
            if valor.lower() == "n":
                cont
            lista.append(valor)
        return lista

    elif tipo == "5":  # Diccionario anidado
        dic = {}
        cont = True
        while cont:
            clave = input("Introduce clave del subdiccionario ('n' para terminar):\n>> ")
            if clave.lower() == "n":
                cont
            subtipo = elegir_tipo_valor()
            dic[clave] = pedir_valor(subtipo)
        return dic


def mostrar_diccionario(dic):
    for k, v in dic.items():
        print(f"{k}: {v}")


def añadir_diccionario_anidado(diccionario_general, nombre_general):
    dic_anidado = {}
    continuar = True
    while continuar:
        menu_diccionario_anidado()
        opcion = input("Elige una opción:\n>> ")

        if opcion == "1":  # Añadir clave
            clave = input("Introduce nombre de la clave:\n>> ")
            if clave in dic_anidado:
                print("Esa clave ya existe.")
            else:
                tipo = elegir_tipo_valor()
                dic_anidado[clave] = pedir_valor(tipo)

        elif opcion == "2":  # Eliminar clave
            clave = input("Introduce clave a eliminar:\n>> ")
            if clave in dic_anidado:
                dic_anidado.pop(clave)
            else:
                print("Esa clave no existe.")

        elif opcion == "3":  # Mostrar
            print("\n--- Diccionario actual ---")
            mostrar_diccionario(dic_anidado)

        elif opcion == "4":  # Finalizar
            dic_anidado["id"] = len(diccionario_general[nombre_general]) + 1
            diccionario_general[nombre_general].append(dic_anidado)
            continuar = False


def eliminar_diccionario_anidado(diccionario_general, nombre_general):
    mostrar_diccionario_general(diccionario_general, nombre_general)
    try:
        id_eliminar = int(input("Introduce el ID del diccionario que quieres eliminar:\n>> "))
        lista = diccionario_general[nombre_general]
        encontrado = next((i for i, d in enumerate(lista) if d.get("id") == id_eliminar), None)
        if encontrado is not None:
            lista.pop(encontrado)
            # Reasignar IDs
            for i, d in enumerate(lista):
                d["id"] = i + 1
            print("Eliminado correctamente.")
        else:
            print("No se encontró ese ID.")
    except ValueError:
        print("Debes introducir un número válido.")


def mostrar_diccionario_general(diccionario_general, nombre_general):
    print(f"\n=== Contenido de {nombre_general} ===")
    lista = diccionario_general[nombre_general]
    if not lista:
        print("(Vacío)")
    else:
        for dic in lista:
            print(f"\nDiccionario ID {dic['id']}:")
            for k, v in dic.items():
                if k != "id":
                    print(f"  {k}: {v}")
    print("-" * 50)


def main():
    nombre_general = input("Introduce el nombre del diccionario general:\n>> ")
    diccionario_general = {nombre_general: []}
    cont = True
    while cont:
        menu_principal_general()
        opcion = input("Selecciona una opción:\n>> ")

        if opcion == "1":
            añadir_diccionario_anidado(diccionario_general, nombre_general)
        elif opcion == "2":
            eliminar_diccionario_anidado(diccionario_general, nombre_general)
        elif opcion == "3":
            mostrar_diccionario_general(diccionario_general, nombre_general)
        elif opcion == "4":
            print("Saliendo del programa...")
            mostrar_diccionario_general(diccionario_general, nombre_general)
            cont = False
        else:
            print("Opción no válida.")


# Ejecutar el programa
main()