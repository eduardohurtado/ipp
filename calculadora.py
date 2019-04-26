def sumar(a , b):
	c = a + b
	return c
def restar(a , b):
	c = a - b
	return c
def multiplicar(a , b):
	c = a * b
	return c
def dividir(a , b):
	c = a / b
	return c
def resto(a , b):
	c = a % b
	return c
def elevar(a , b):
	c = a ** b
	return c

#continua en el bloque siguiente ->
if __name__ == "__main__":
	numero_1=10
	numero_2=3

	s = sumar(numero_1,numero_2)
	r = restar(numero_1,numero_2)
	m = multiplicar(numero_1,numero_2)
	d = dividir(numero_1,numero_2)
	mo = resto(numero_1,numero_2)
	e = elevar(numero_1,numero_2)

#mostremos la informacion obtenida
print('la suma es :' + str(s))
print('la resta es :' + str(r))
print('la multiplicacion es :' + str(m))
print('la division es :' + str(d))
print('el resto es :' + str(mo))
print('el numero a elevador b es :' + str(e))