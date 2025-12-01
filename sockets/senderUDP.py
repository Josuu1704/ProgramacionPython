import socket as sk
import time
import pickle

sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

sock.connect(("127.0.0.1", ))

salir = False
while not salir:
    mensaje = "holaaaa"
    #diccionario = {"hola":"adios"}
    sock.send(mensaje.encode())
    #sock.send(pickle.dumps(diccionario))
    print("El mensaje está enviado")
    time.sleep(1)
    if mensaje == "salir":
        salir = True