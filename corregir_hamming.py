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
            if numero not in (0, 1) and len(mensaje) == 7:
                valido = False
                break
        if valido:
            break
        else:
            print("El mensaje que has introducido no es correcto")

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
    filas = len(general)
    columnas = len(general[0])

    for i in range(columnas):
        numero = int(general[0][i])
        suma = 0
        for j in range(filas):
            if j != 0 and general[j][i] != "?" and int(general[j][i]) != numero:
                suma += 1
        if suma == 2:
            if int(general[0][i]) == 0:
                general[0][i] = "1"
            else:
                general[0][i] = "0"


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
