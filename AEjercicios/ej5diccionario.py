"""
2. Haz el rpograma anterior escalable a un diccionario general con un nombre
escogido por el usuario, por ejemplo "biblioteca" cuyo valor sea un array de diccionarios
que tiene el sistema previo de inroduccion de informacion
"""


def validarNumero(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def obtener_valor_validado():
    tipos_validos = ['str', 'int', 'otros']
    tipo_es_valido = False
    tipo = ""

    while not tipo_es_valido:
        tipo = input(f"Elige el tipo de valor (int, str, bool")
        if tipo in tipos_validos:
            tipo_es_valido = True
        else:
            print("El valor es invalido....")

    valor_es_valido = False
    valor_str = ""

    while not valor_es_valido:
        valor_str = input(f"Dame el valor elegido: {tipo}): ")
        if tipo == 'int':
            if validarNumero(valor_str):
                valor_es_valido = True
                return int(valor_str)
            else:
                print("El valor debe ser un número entero.")
        else:
            valor_es_valido = True
            return valor_str

def crear_diccionario_individual():
    diccionario_custom = {}
    continuar_clave_valor = True
    while continuar_clave_valor:
        clave = input("Clave: ")
        valor = obtener_valor_validado()
        diccionario_custom[clave] = valor
        if "s" != input("¿Añadir otra clave/valor? (s/n)"):
            continuar_clave_valor = False
    return diccionario_custom

nombre_gen = input("Nombre del diccionario general: ")
datos_gen = {}
datos_gen[nombre_gen] = []
continuar_diccionario = True
while continuar_diccionario:
    nuevo_elemento = crear_diccionario_individual()
    if nuevo_elemento:
        datos_gen[nombre_gen].append(nuevo_elemento)
    if "s" != input("¿Añadir otro elemento completo? (s/n)"):
        continuar_diccionario = False
print(datos_gen)
