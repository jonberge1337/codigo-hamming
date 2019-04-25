salto = 1
cadena_auto = "??1?010?101"
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
