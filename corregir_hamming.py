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
    calcular si es potencia o no
    """
    while numero > 1:
        numero /= 2
    return numero == 1


def array_pos(lista, salto):
    """
    creamos el array de cada posicion
    """
    tamaino = len(lista)
    lista_temporal = []
    # recortamos la cadena para que empiece en ese elemento
    lista = lista[salto-1:]
    # agregamos una varible apoyo para conservar las "coordenadas"
    vacios = "?" * (salto-1)
    lista_temporal += vacios

    vacios = "?" * salto
    nsalto = salto * 2
    while len(lista) > 0:
        # tomamos los elementos segun la paridad
        lista_temporal += lista[:salto]
        # brincamos los elementos segun la paridad
        lista = lista[nsalto:]
        # agregamos una varible apoyo para conservar las coordenadas
        lista_temporal += vacios

    # truncamos hasta el largo de la cadena con paridad
    lista_temporal = lista_temporal[:tamaino]

    return lista_temporal


def array_general(lista):
    """
    creamos el array general para despues corregir
    """
    general = []
    tamaino = len(lista)
    general.append(lista[:])
    for i in range(tamaino):
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
        # return lista.count("?") == len(ant) and (lista.count("1") == len(pos) or lista.count("1") == len(pos))
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

    def gen_columna(lista, indice):
        return lista[1][indice], lista[2][indice], lista[3][indice], lista[4][indice]

    filas = len(general)
    columnas = len(general[0])
    impares = 0
    posiciones = []
    antiposi = []
    for i in range(1, filas):
        if es_impar(general[i]):
            impares += 1
            # le quitamos uno a i para que luego no se pase de rango
            # en la tupla generada
            posiciones.append(i-1)
        else:
            antiposi.append(i-1)

    for i in range(columnas):
        columna = gen_columna(general, i)
        if iguales(columna, posiciones, antiposi):
            if general[0][i] == "1":
                general[0][i] = "0"
            else:
                general[0][i] = "1"

    # for i in range(columnas):
    #     columna = []
    #     for j in range(filas):
    #         columna.append(general[j][i])
    #         if iguales(columna, posiciones, antiposi):
    #             if general[0][i] == "1":
    #                 general[0][i] = "0"
    #             else:
    #                 general[0][i] = "1"


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
