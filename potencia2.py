#!/usr/bin/env python


def posicion(numero):
    """
    esta 2 elevado
    """
    loes = False
    mult = 1
    while mult < numero:
        mult *= 2
    if mult == numero:
        loes = True

    return loes


def pedir_numero():
    """
    pedimos numero validado
    """
    while True:
        try:
            numero = int(input("Introduce un numero mayor que 0: "))
        except ValueError:
            numero = -1
        if numero > 0:
            break

    return numero


def lista_bits():
    """
    crear lista de bits
    """
    print("Cuantos bits vas a meter?: ")
    cantidad = pedir_numero()
    lista = []
    for i in range(cantidad):
        print("Introduce el bit numero", i)
        lista.append(pedir_numero())

    return lista


def lista_rellena(lista_bits):
    posicion = 0
    lista = []
    # for i


if __name__ == "__main__":
    VERDADERO = posicion(int(input("Introduce un numero: ")))
    print(VERDADERO)
