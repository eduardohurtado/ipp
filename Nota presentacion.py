#!/usr/bin/env python

print("Calculemos la nota de presentación. \n")
print('Ingrese las notas de las tareas de Laboratorio: \n')

lab1 = float(input("1ra tarea "))
lab2 = float(input("2da tarea "))
lab3 = float(input("3ra tarea "))

notalab = ((lab1+lab2+lab3) / 3) * 0.15

print(notalab)

print('Ingrse las notas de las tareas en clase: \n')
clase1 = float(input("1ra tarea "))
clase2 = float(input("2da tarea "))
clase3 = float(input("3ra tarea "))

notaclas = ((clase1+clase2+clase3) / 3) * 0.15

print(notaclas)

print('Ingrse las notas de las evaluaciones Solemnes: \n')
solemne1 = float(input("1r solemne "))
solemne2 = float(input("2do solemne "))

notapres = float((solemne1 * 0.35)) + float((solemne2 * 0.35)) + float(notalab) + float(notaclas)

print ("La nota de presentación final es " + str(notapres))
