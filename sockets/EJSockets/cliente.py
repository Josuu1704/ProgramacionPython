import socket as sk
sock = sk.socket(sk.AF_INET,sk.SOCK_DGRAM)

salir = False
while not salir:
    remitente = input("Introduce el nombre del remitente -> \n")
    mensaje = input("Escribe el mensaje que quieres enviar -> \n")

    if mensaje == "salir":
        salir = True
    else:
        mensaje_completo = f"{remitente}:{mensaje}"
        sock.sendto(mensaje_completo.encode(), ("127.0.0.1", 8000))
        print("El mensaje esta enviado")