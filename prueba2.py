salto = 1
lista = list("11010110010")
tamaino = len(lista)
lista_temporal = []
# recortamos la cadena para que empiece en ese elemento
lista = lista[salto-1:]
# agregamos una varible apoyo para conservar las "coordenadas"
vacios = "N" * (salto-1)
lista_temporal += vacios
vacios = "N" * salto
nsalto = salto * 2
while len(lista) > 0:
    # tomamos los elementos segun la paridad
    lista_temporal += lista[:salto]
    # brincamos los elementos segun la paridad
    lista = lista[nsalto:]
    # agregamos una varible apoyo para conservar las coordenadas
    lista_temporal += vacios
# truncamos hasta el largo de la cadena con paridad
lista_temporal = lista_temporal[:len(tamaino)]