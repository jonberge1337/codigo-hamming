#!/usr/bin/env python


def pedir_numero():
    """
    pedir numero valido
    """
    while True:
        valido = True
        mensaje = input("Introduce el mensaje: ")
        for i in mensaje:
            try:
                numero = int(i)
            except ValueError:
                numero = 2
            if numero not in (0, 1):
                valido = False
                break
        if valido:
            break
        else:
            print("El mensaje que has introducido no es correcto")

    return mensaje
