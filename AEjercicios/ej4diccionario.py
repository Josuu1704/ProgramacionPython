"""
1. Crea un programa que permita al usuario crear un diccionario custom.
Permitele elegir el nombre de la clave, el tipo y que llene ambas
"""


def validarNumero(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def obtener_valor():
    valores_validos = ['str', 'int', 'bool']
    tipo_es_valido = False
    tipo = ""

    while not tipo_es_valido:
        tipo = input(f"Elige el tipo de valor (int, str, bool")
        if tipo in valores_validos:
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

custom = {}
continuar = True

while continuar:
    clave = input("Dime la clave: ")
    valor = obtener_valor()
    custom[clave] = valor
    if "s" != input("¿Desea seguir añadiendo elementos? (s/n)"):
        continuar = False

print("Diccionario final:")
print(custom)
