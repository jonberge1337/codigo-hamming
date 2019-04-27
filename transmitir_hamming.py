#!/usr/bin/env python


def pedir_numero():
    """
    pedir numero valido
    """
    while True:
        valido = True
        mensaje = input("Introduce 7 bits: ")
        for i in mensaje:
            try:
                numero = int(i)
            except ValueError:
                numero = 2
            if numero not in (0, 1) and len(mensaje) == 7:
                valido = False
                break
        if valido:
            break
        else:
            print("Los bits no son correctos")

    return mensaje


def potencia(numero):
    """
    calcular si es potencia de 2 o no
    >>> potencia(8)
    True
    >>> potencia(7)
    False
    """
    while numero > 1:
        numero /= 2
    return numero == 1


def crear_array(mensaje, cantidadpos):
    """
    crearemos un array pero sin importar los numero de paridad
    >>> crear_array("1010101", 4)
    ["?", "?", "1", "?", "0", "1", "0", "?", "1", "0", "1"]
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


def es_par(lista, salto):
    """
    nos dira si es par o no la posicion
    dependiendo la cantidad del salto que le pasemos
    >>> es_par(["?", "?", "1", "?", "0", "1", "0", "?", "1", "0", "1"], 1)
    # lo convertiria en un array de 1 salto
    # ["?", "1", "0", "0", "1", "1"]
    # se suman todos los 1 y alfinal devuelve el booleno
    False
    """
    lista_temporal = []
    tamaino = len(lista)
    lista = lista[salto-1:]

    nsalto = salto * 2

    while len(lista) > 0:
        # con esto extraemos los bit necesarios
        lista_temporal += lista[:salto]
        # con esto quitamos los bits extraidos mas su doble
        lista = lista[nsalto:]

    lista_temporal = lista_temporal[:tamaino]

    suma = sum([1 for i in lista_temporal if i == "1"])

    return suma % 2 == 0


def solucionar_hamming(lista):
    """
    quitamos los interrogantes y le ponemos los numero de paridad
    llamamos a la funcion es_par para saber con que numero sustituir
    """
    tamaino = len(lista)
    for i in range(tamaino):
        if lista[i] == "?":
            if es_par(lista[:], i + 1):
                lista[i] = "0"
            else:
                lista[i] = "1"


def main():
    numero = pedir_numero()
    cantidad = 4
    array = crear_array(numero, cantidad)
    # print("".join(array))
    solucionar_hamming(array)
    print("El codigo hamming con los bits de paridad: ", end='')
    print("".join(array))


if __name__ == "__main__":
    main()
