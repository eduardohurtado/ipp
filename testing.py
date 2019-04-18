#!/usr/bin/env python
def fibonacci(num):
	fib = 0 #esta es la variable que tendra que contener el resultado al final de la funcion
	# Aqui escribir el desarrollo de las funcion
	a = 1
	c = 0

	for i in range(num):
		c = fib
		fib = a + fib
		a = c

	return fib

if __name__ == '__main__':

	print("La serie fibonacci esta retornando: ", end="")
	print(fibonacci(10)) #si se ingresa 10 el resultado debe ser: 34