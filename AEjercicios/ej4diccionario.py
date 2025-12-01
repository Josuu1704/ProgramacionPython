custom = {}

def esString():
    valor = input("Introduce valor: \n>> ")
    return valor

def esInt():
    valor = float(input("Introduce valor: \n>> "))
    return valor

def esLista():
    valores = []
    otro = True
    while otro:
        valor = input("Introduce Valores ('n' para terminar): \n>> ")
        if valor == "n":
            otro = False
        else:
            valores.append(valor)
    return valores

def esDiccionario():
    valores = {}
    clave = input("Introduce clave: \n>> ")
    print("-------- Valores --------\n1. String\n2. Int\n3. Lista\n4. Diccionario")
    tipo = int(input("Introduce tipo de valor: \n>> "))
    if tipo == 1:
        valor = esString()
        valores[clave] = valor
    elif tipo == 2:
        valor = esInt()
        valores[clave] = valor
    elif tipo == 3:
        valor = esLista()
        valores[clave] = valor
    elif tipo == 4:
        valor = esDiccionario()
        valores [clave] = valor
    return valores

def mostrar(diccionario):
    for k, v in diccionario.items():
        print(f"{k}: {v}")

def mostrarDiccionario(diccionario):
    keyDictionary = input("Introduce nombre de la clave del diccionario:\n>> ")
    if keyDictionary in diccionario:
        print(f"{keyDictionary}:")
        for k, v in diccionario[keyDictionary].items():
            print(f"\t{k}: {v}")

def menuAñadir():
    clave = input("Introduce clave: \n>> ")
    print("-------- Valores --------\n1. String\n2. Int\n3. Lista\n4. Diccionario")
    tipo = int(input("Introduce tipo de valor: \n>> "))
    if tipo == 1:
        valor = esString()
        custom[clave] = valor
    elif tipo == 2:
        valor = esInt()
        custom[clave] = valor
    elif tipo == 3:
        valor = esLista()
        custom[clave] = valor
    elif tipo == 4:
        valor = esDiccionario()
        custom[clave] = valor

def menuMostrarDiccionarios():
    LoD = int(input("--- Mostrar ---\n1. Clave y Valor / Lista\n2. Diccionario\n>> "))
    if LoD == 1:
        mostrar(custom)
    elif LoD == 2:
        mostrarDiccionario(custom)

def eliminarDiccionario(diccionario):
    eliminar = input("Introduce clave a eliminar: \n>> ")
    if eliminar in diccionario:
        diccionario.pop(eliminar)

continuar = True
while continuar:
    print("-------------------- Diccionario Custom --------------------")
    hacer = int(input("1. Añadir a diccionario. \n2. Borrar de Diccionario. \n3. Mostrar Diccionario. \n4. salir\n>> "))
    if hacer == 1:
        menuAñadir()
    elif hacer == 2:
        eliminarDiccionario(custom)
    elif hacer == 3:
        menuMostrarDiccionarios()
    elif hacer == 4:
        continuar = False
        mostrar(custom)
    else:
        print("Error, dato incorrecto.")