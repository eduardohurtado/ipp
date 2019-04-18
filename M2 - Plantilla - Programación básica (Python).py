#!/usr/bin/env python

def fibonacci(num):
    fib = 0 #esta es la variable que tendra que contener el resultado al final de la funcion
    # Aqui escribir el desarrollo de las funcion
    a = 1  
    c = 0 # Primea posicion secuencia
    for i in range(num):        # Se comienza el rango
        c = fib                 # Rango parte de 0 
        fib = a + fib           # Se suma el ultimo numero a la secuencia
        a = c                   # Cambia numero a sumar 

    return fib # En el ejemplo es 55 ya que parte 0 como primera posicion de la secuencia

def mcm(a,b):
    mcm = 0 #esta es la variable que tendra que contener el resultado al final de la funcion
    # Aqui escribir el desarrollo de las funcion
    if a > b:                       # tomamos el numero mayor para partir desde ahí probando numeros buscando mod=0
        mayor = a
    else:
        mayor = b
    while(True):                    # comprobamos si hay resto entre la variable "mayor" y cada numero
        if((mayor % a == 0) and (mayor % b == 0)):
            mcm = mayor
            break                   # al cumplirse ambas condiciones se termina el ciclo
        mayor += 1                  # si no se cumple se suma 1 a la variable "mayor"
    return mcm 

def mcd(a, b):
    mcd = 0 #esta es la variable que tendra que contener el resultado al final de la funcion
    # Aqui escribir el desarrollo de las funcion
    while (b>0):                    # Se repite mientras b sea mayor que 0
        mcd = b                     # toma el valor del segundo numero
        b = a % b                   # se saca el resto entre las variables 
        a = mcd                     # se iguala al resultado de b para retomar el calculo
        
    return mcd

def reverse_num(num):
    reverse = 0 #esta es la variable que tendra que contener el resultado al final de la funcion
    # Aqui escribir el desarrollo de las funcion
    reverse = str(num)[::-1]        # se castea a str para poder mmodificar y se lista de forma inversa

    return reverse

def reverse_text(text):
    reverse = "" #esta es la variable que tendra que contener el resultado al final de la funcion
    # Aqui escribir el desarrollo de las funcion
    reverse = text[::-1]            # Lo mismo que el ejercicio anterior pero aqui no es necesario castear

    return reverse

def palindromo(text):
    # Aqui escribir el desarrollo de las funcion

    if (str(text)[::-1] == str(text)):          # se da vuelta el numero, casteado a string, y se compara con el numero ingresado, 
                                                # tambien casteado para poder comparar
        return True
    else:
        return False

def num_mayores(num):
    n_mayores = 0 #esta es la variable que se tendra que tener el resultado al final de la funcion
    # Aqui escribir el desarrollo de las funcion
    if (num%2 != 0):                                # Se verifica si el nuemro ingresado es par o impar
        num -= 1                                    # si impar se resta 1
    else:
        pass
    lista_num = list(range(num+2,num+22,2))         # se genera la lista con los 10 numeros pares siguientes
    n_mayores= lista_num[9]                         # se asigna el valor de la decima posicion a la variable n_mayores

    return n_mayores

def factorial(num):
    fact = 1 #esta es la variable que se tendra que tener el resultado al final de la funcion
    # Aqui escribir el desarrollo de las funcion
    for i in range(1, num + 1):             # Generamos el rango
        fact = fact * i                     # Se multiplican uno a uno
    return fact

def primo(num):
    # Aqui escribir el desarrollo de las funcion
    # Un primo se divide solo por 1 y el mismo numero asi que se realiza esa comprobacion

    divisores = 0                           # acumulador de divisores
    for i in range(1, num + 1):             # Se parte desde 1 hasta el numero +1
        if num % i == 0:                    # Se comprueba que no haya resto
            divisores += 1                  # Si no hay se suma un divisor
    if(divisores == 2):
        return True                         # Si son solo 2 los divisores true, si no false
    else:
        return False


def equi_parentesis(text):
    # Aqui escribir el desarrollo de las funcion
    # Contar (
    abre = text.count("(")
    # Contar )
    cierra = text.count(")")

    # Comparar
    if (abre == cierra): #Cambie este True por la condicion que deba tener para su funcion retorne un valor correcto
        return True
    else:
        return False


def get_fecha(fecha):
    #si el formato es DDMMAAAA
    dia = 0 #estas son las variable que tendran que contener los resultados al final de la funcion
    mes = 0
    ano = 0
    # Aqui escribir el desarrollo de las funcion
    fecha =str(fecha) # casteo a str para poder trabajarlo
    # se devuelven los indices solicitados en formato entero
    dia = int(fecha[0:2]) 
    mes = int(fecha[2:4])
    ano = int(fecha[4:])

    return dia,mes,ano

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
        diaact += 30                                                # se suma un mes completo a la variable dia actial  
        mesact -= 1                                                 # y se resta un mes

    if (mesact < mesnac):                                           # Lo mismo con los meses
        mesact += 12
        anoact -= 1

    dia_total = diaact - dianac                                     # Sacamos las diferencias entre los valores obtenidos 
    mes_total = mesact - mesnac
    ano_total = anoact - anonac

    total_dia = dia_total + (mes_total * 30) + (ano_total * 365)    # Se calcula el total de dias
    horas_dias = total_dia * 24                                     # Total de horas
    min_dias = horas_dias * 60                                      # Total de minutos

    return min_dias, horas_dias, total_dia



if __name__ == '__main__':
    #El programa esta programado para que al momento de ejecutarse, imprima todos los resultados de todas las funciones
    # cada funcion vendra con un caso de prueba, en el cual estara comentado su resultados

    #IMPORTANTE: NO SE CONFIEN CON SOLO TENER EL CASO DE PRUEBA. SIN EMBARGO USTEDES IGUAL PUEDEN
    #CAMBIAR LOS PARAMETROS PARA REALIZAR SUS PROPIAS PRUEBAS
    print("La serie fibonacci esta retornando: ", end="")
    print(fibonacci(10)) #si se ingresa 10 el resultado debe ser: 34
    print("El MCM esta retornando: ", end="")
    print(mcm(20,14)) #si se ingresa 20,14 el resultado debe ser: 140
    print("El MCD esta retornando: ", end="")
    print(mcd(20,14)) #si se ingresa 20,14 el resultado debe ser: 2
    print("El numero ingresado al revez es: ", end="")
    print(reverse_num(123456789)) #si se ingresa 123456789 el resultado debe ser: 987654321
    print("La palabra ingresada al revez es: ", end="")
    print(reverse_text("abcdef")) #si se ingresa "abcdef" el resultado debe ser: fedcba
    print("El resultado si un numero es palindromo es: ", end="")
    print(palindromo(1234321)) #si se ingresa 1234321 el resultado debe ser: True
    print("El ultimo numero de la seria de los 10 mayores es: ", end="")
    print(num_mayores(15)) #si se ingresa 15 el resultado debe ser: 34
    print("El resultado de factorial es: ", end="")
    print(factorial(10)) #si se ingresa 10 el resultado debe ser: 3628800
    print("El resultado del numero si es primo es: ", end="")
    print(primo(7)) #si se ingresa 7 el resultado debe ser: True
    print("El resultado de estar equilibrado de parentesis es: ", end="")
    print(equi_parentesis("(sasa(asdsa)))")) #si se ingresa "(sasa(asdsa)))" el resultado debe ser: False
    print("La tupla de la fecha separada es: ", end="")
    print(get_fecha(25072017)) #si se ingresa 25072017 el resultado debe ser: (25, 7, 2017)
    print("La tupla de los minutos de mi vida es: ", end="")
    print(min_vivido(25072017,11101982)) #si se ingresa 25072017,11101982 el resultado debe ser: (17802720, 296712, 12363)
