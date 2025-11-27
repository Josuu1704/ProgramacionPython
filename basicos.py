#int, str, floar, list
#input(), len()
nombreVariable = "200"
nombreVariable = 2
nombreVariable = str(nombreVariable)

print()
print(nombreVariable)
print()
print(type(nombreVariable))

#input(), len()
print()
nombre = input("Dime tu nombre: ")
print(f"Hola {nombre}")
print(len(nombre))

# ==, !=, >, <, >=, <=, and, or, not
apellidoToponimico = False
num = 3

if num < 5:
    print("~~~~~~~~~~~~~~~~")
    print("~~~~ENHORABUENA~~~~")
    print("~~~~~~~~~~~~~~~~")

    if num > 0:
        print("~~~~~~~~~~~~~~~~")
        print("~~~~FELICITACIONES~~~~")
        print("~~~~~~~~~~~~~~~~")

elif num < 10:
    print("~~~~~~~~~~~~~~~~")
    print("~~~~MUY MAL~~~~")
    print("~~~~~~~~~~~~~~~~")
