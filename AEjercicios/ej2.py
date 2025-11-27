#Calculadora con bucle
# Menu y operacion: Suma, resta, mul, div
# Salga si el usuario pide salir en el menu

num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))
op = int(input("Introduce que operacion quiers realizar: \n1. Suma \n2. Resta \n3. Division \n4. Multiplicacion\n"))

salir = True

while (salir and op < 5):
    if op == 1:
        suma = num1 + num2
        print(f"La suma es: {suma}")
        salir = False
    elif op == 2:
        resta = num1 - num2
        print(f"La resta es: {resta}")
        salir = False
    elif op == 3:
        mul = num1 * num2
        print(f"La mul es {mul}")
        salir = False
    elif op == 4:
        div = num1 / num2
        print(f"La division es {div}")
        salir = False
else:
    salir = False


