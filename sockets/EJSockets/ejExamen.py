"""
 Sistema de Mensajería con UDP
Descripción
Crea un programa que simule un sistema de mensajería en el que un cliente envía un mensaje a un servidor. El servidor guarda los mensajes en un array bidimensional, donde cada fila corresponde a un mensaje y la columna 0 contiene el mensaje en sí, mientras que la columna 1 contiene el remitente. El servidor debe devolver un diccionario con el número de mensajes almacenados y el último mensaje recibido.
Requerimientos
Servidor: debe recibir mensajes mediante sockets UDP y almacenarlos en un array bidimensional.
Cliente: debe enviar mensajes al servidor y manejar errores en caso de que el servidor no esté disponible.
Uso de excepciones: manejar errores al enviar y recibir mensajes.
"""

import socket as sk


historial = []

sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
sock.bind(("127.0.0.1",))

salir = False
while not False:
    datos, direccion = sock.recvfrom(1024)
    mensaje_completo = datos.decode()

    remitente, mensaje = mensaje_completo.split(":", 1)
    historial.append([mensaje, remitente])

    respuesta = {
        "total_mensajes": len(historial),
        "ultimo_mensaje": historial[-1][0]
    }

    respuesta_str = f"Total: {respuesta['total_mensajes']}, Último: {respuesta['ultimo_mensaje']}"
    sock.sendto(respuesta_str.encode(), direccion)

    print("Servidor cerrado.")
    sock.close()