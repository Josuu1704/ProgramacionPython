import socket as sk

sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
sock.bind(("127.0.0.1", 12500))

sock.listen(1)
print("El recibidor está esperando...")

connection, direccion = sock.accept()
print(f"Conectado con {direccion}")

salir = False
while not salir:
    datos = connection.recv(1024)
    if not datos:
        salir = True
    print(f"Llega la siguiente información:\n {datos.decode()}")

connection.close()