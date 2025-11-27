# 4. Realiza un programa de cambio de divisas euro-latam. Almacenaremos en una tabla los cambios respecto al euro. La idea es que una
# vez el usuario introduzca una cantidad de euros y la moneda a la que quiere cambiar, y le devuelva la cantidad cambiada.

# Bolívar Venezolano - 202,78
# Guaraní Paraguayo - 8.336,03
# Peso Argentino - 1.564,31
# Peso Boliviano - 8,0736
# Peso Chileno - 1.120,74
# Peso Colombiano - 4.562,79
# Peso Uruguayo - 46,602
#Real Brasileño - 6,2661
# Sol Peruano - PEN - 4,0908

print("Cambio de DIVISA")

Paises = [
    "1. Venezuela",
    "2. Paraguay",
    "3. Argentina",
    "4. Bolivia",
    "5. Chile",
    "6. Colombia",
    "7. Uruguay",
    "8. Brasil",
    "9. Perú",
    "10. Salir"
]

salir = False

while not salir:
    print("Cambio de moneda:")
    for pais in Paises:
        print(pais)

    option = int(input("Elige el país por el cual cambiar la moneda (número): "))

    if option == 1:
        cantidad = float(input("Introduce la cantidad que deseas cambiar: "))
        resultado = cantidad * 202.78
        print(f"Usted recibe {resultado:.2f} Bolívares venezolanos.")
    elif option == 2:
        cantidad = float(input("Introduce la cantidad que deseas cambiar: "))
        resultado = cantidad * 8336.03
        print(f"Usted recibe {resultado:.2f} Guaraníes paraguayos.")
    elif option == 3:
        cantidad = float(input("Introduce la cantidad que deseas cambiar: "))
        resultado = cantidad * 1564.31
        print(f"Usted recibe {resultado:.2f} Pesos argentinos.")
    elif option == 4:
        cantidad = float(input("Introduce la cantidad que deseas cambiar: "))
        resultado = cantidad * 8.0736
        print(f"Usted recibe {resultado:.2f} Bolivianos.")
    elif option == 5:
        cantidad = float(input("Introduce la cantidad que deseas cambiar: "))
        resultado = cantidad * 1120.74
        print(f"Usted recibe {resultado:.2f} Pesos chilenos.")
    elif option == 6:
        cantidad = float(input("Introduce la cantidad que deseas cambiar: "))
        resultado = cantidad * 4562.79
        print(f"Usted recibe {resultado:.2f} Pesos colombianos.")
    elif option == 7:
        cantidad = float(input("Introduce la cantidad que deseas cambiar: "))
        resultado = cantidad * 46.602
        print(f"Usted recibe {resultado:.2f} Pesos uruguayos.")
    elif option == 8:
        cantidad = float(input("Introduce la cantidad que deseas cambiar: "))
        resultado = cantidad * 6.2661
        print(f"Usted recibe {resultado:.2f} Reales brasileños.")
    elif option == 9:
        cantidad = float(input("Introduce la cantidad que deseas cambiar: "))
        resultado = cantidad * 4.0908
        print(f"Usted recibe {resultado:.2f} Soles peruanos.")
    elif option == 10:
        salir = True
        print("Saliendo del programa...")
    else:
        print("Opción no válida.")
