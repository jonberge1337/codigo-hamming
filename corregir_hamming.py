#!/usr/bin/env python


def pedir_numero():
    """
    pedir numero valido
    """
    while True:
        valido = True
        mensaje = input("Introduce 11 bits: ")
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


def array_pos(lista, salto):
    """
    creamos un array dependiendo del salto que tiene que hacer
    >>> array_pos(["0", "0", "0", "0", "1", "1", "0", "0", "0", "0", "0"], 1)
    ["0", "?", "0", "?", "1", "?", "0", "?", "0", "?", "0"]
    """
    tamaino = len(lista)
    lista_temporal = []

    # recortamos la cadena para que empiece en ese elemento
    lista = lista[salto-1:]

    # añadimos una variable apoyo para conservar todas las posiciones
    vacios = "?" * (salto-1)
    lista_temporal += vacios

    vacios = "?" * salto
    nsalto = salto * 2
    while len(lista) > 0:
        # tomamos los elementos segun la paridad
        lista_temporal += lista[:salto]
        lista_temporal += vacios

        # quitamos la informacion copiada mas la vacia
        lista = lista[nsalto:]

    # recortamos la lista al tamaño de la lista original
    # para no tener ? de sobra
    lista_temporal = lista_temporal[:tamaino]

    return lista_temporal


def array_general(lista):
    """
    creamos el array general para despues corregir
    >>> array_general(["0", "0", "0", "0", "1", "1", "0", "0", "0", "0", "0"])
    [
        ["0", "0", "0", "0", "1", "1", "0", "0", "0", "0", "0"]
        ["0", "?", "0", "?", "1", "?", "0", "?", "0", "?", "0"]
        ["?", "0", "0", "?", "?", "1", "0", "?", "?", "0", "0"]
        ["?", "?", "?", "0", "1", "1", "0", "?", "?", "?", "?"]
        ["?", "?", "?", "?", "?", "?", "?", "0", "0", "0", "0"]
    ]
    """
    general = []
    tamaino = len(lista)
    general.append(lista[:])
    for i in range(1, tamaino):
        if potencia(i):
            general.append(array_pos(lista, i))

    return general


def corregir(general):
    """
    con esta funcion comprobamos si esta correcto
    en caso de que no lo este lo corregimos
    """
    def es_impar(lista):
        return sum([int(i) for i in lista if i.isdigit()]) % 2 != 0

    def iguales(lista, pos, ant):
        igual = True
        for i in pos:
            if lista[i] == "?":
                igual = False
                break

        for i in ant:
            if lista[i] != "?":
                igual = False
                break
        return igual

    filas = len(general)
    columnas = len(general[0])
    impares = 0
    posiciones = []
    antiposi = []
    for i in range(1, filas):
        if es_impar(general[i]):
            impares += 1
            # le quitamos uno a i para que luego no se pase de rango
            # en la lista de columnas generada porque la general tendra
            # 5 filas y las columnas que analizamos son 4
            posiciones.append(i-1)
        else:
            antiposi.append(i-1)

    for i in range(columnas):
        columna = [general[j][i] for j in range(1, len(general))]
        if iguales(columna, posiciones, antiposi):
            if general[0][i] == "1":
                general[0][i] = "0"
            else:
                general[0][i] = "1"


def main():
    array = pedir_numero()
    array = list(array)
    general = array_general(array)
    corregir(general)
    print("secuencia metida", "".join(array))
    print("secuencia final", "".join(general[0]))
    for i in general:
        print("".join(i))


if __name__ == "__main__":
    main()
