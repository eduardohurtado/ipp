#!/usr/bin/env python
def min_vivido(fech_act,fec_nac):
    min_dias = 0 #estas son las variable que tendran que contener los resultados al final de la funcion
    horas_dias = 0
    total_dia = 0
    # Aqui escribir el desarrollo de las funcion
    fech_act = str(fech_act)                                        #Se castean las variables para manipularlas
    fec_nac = str(fec_nac)
    # El dia tiene 1440 minutos
    diaact = int(fech_act[0:2])                                     #Se toman los dias, meses y años dejandolos como enteros
    mesact = int(fech_act[2:4])
    anoact = int(fech_act[4:])

    dianac = int(fec_nac[0:2]) 
    mesnac = int(fec_nac[2:4])
    anonac = int(fec_nac[4:])

    if (diaact < dianac):                                           # Cuando el dia de nacimiento es mayor al dia actual 
        diaact = diaact + 30                                        # se suma un mes completo a la variable dia actial  
        mesact = mesact - 1                                         # y se resta un mes

    if (mesact < mesnac):                                           # Lo mismo con los meses
        mesact = mesact + 12
        anoact = anoact - 1

    dia_total = diaact - dianac                                     # Sacamos las diferencias entre los valores obtenidos 
    mes_total = mesact - mesnac
    ano_total = anoact - anonac

    total_dia = dia_total + (mes_total * 30) + (ano_total * 365)    # Se calcula el total de dias
    horas_dias = total_dia * 24                                     # Total de horas
    min_dias = horas_dias * 60                                      # Total de minutos

    return min_dias, horas_dias, total_dia



if __name__ == '__main__':

    print("La tupla de los minutos de mi vida es: ", end="")
    print(min_vivido(25072017,24072017)) #si se ingresa 25072017,11101982 el resultado debe ser: (17802720, 296712, 12363)