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


def paridad(mensaje):
    """
    cuantos bits necesita de paridad
    """
    cantidad = 1
    elevado = 1
    while elevado < len(mensaje):
        elevado *= 2
        cantidad += 1

    return cantidad


def potencia(numero):
    """
    calcular si es potencia o no
    """
    while numero > 1:
        numero /= 2
    return numero == 1


def crear_array(mensaje, cantidadpos):
    """
    crearemos un array pero sin importar los numero de paridad
    """
    total = len(mensaje) + cantidadpos
    lista = []
    j = 0
    for i in range(total):
        if potencia(i + 1):
            lista.append("?")
        else:
            lista.append(mensaje[j])
            j += 1

    return lista


def es_par(cadena_auto, salto):
    """
    nos dira si es par o no
    """
    cadena_temporal = ""
    original_cadena_auto = cadena_auto
    cadena_auto = cadena_auto[salto-1:]

    nduplicado = "N"*(salto-1)
    cadena_temporal += nduplicado

    nduplicado = "N"*salto
    nsalto = salto * 2

    while len(cadena_auto) > 0:
        cadena_temporal += cadena_auto[:salto]

        cadena_auto = cadena_auto[nsalto:]

        cadena_temporal += nduplicado

    cadena_temporal = cadena_temporal[:len(original_cadena_auto)]

    suma = sum([1 for i in cadena_temporal if i == "1"])

    return suma % 2 == 0


def solucionar_hamming(lista):
    """
    quitamos los interrogantes y le ponemos los numero de paridad
    """
    tamaino = len(lista)
    cadena = "".join(lista[:])
    for i in range(tamaino):
        if lista[i] == "?":
            if es_par(cadena, i + 1):
                lista[i] = "0"
            else:
                lista[i] = "1"


if __name__ == "__main__":
    NUMERO = "1010101"       #pedir_numero()
    CANTIDAD = paridad(NUMERO)
    array = crear_array(NUMERO, CANTIDAD)
    print("".join(array))
    solucionar_hamming(array)
    print("".join(array))
