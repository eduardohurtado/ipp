#!/usr/bin/env python

#Ingreso del rut de una sola vez.
rut = input('Ingrese el RUT sin guión ni digito verificador \nSi es menor a diez millones anteponga un 0: ')
#reverso = (rut[::-1])

n1 = (3 * int(rut[0]))
n2 = (2 * int(rut[1]))
n3 = (7 * int(rut[2]))
n4 = (6 * int(rut[3]))
n5 = (5 * int(rut[4]))
n6 = (4 * int(rut[5]))
n7 = (3 * int(rut[6]))
n8 = (2 * int(rut[7]))

suma = n1+n2+n3+n4+n5+n6+n7+n8

resto = suma%11

verificador =11-resto

if verificador == 10: print ("El digito verificador es: K")
elif verificador == 11: print ("El digito verificado es: 0")
else: print ("El digito verificador es: " + str(verificador))
