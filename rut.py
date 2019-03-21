# Sebastián Zapata
# Obtener dígito verificador de RUTS CHILENOS / CHILEAN ID
# Input: Un numero entero sin guión ni dígito verificador.

# extraerDigitoDesdeDerecha: int int -> int
# Dado un número y una posición, devuelve el digito ubicado en la posición de derecha a izquierda del número.
# Ejemplo: extraerDigitoDesdeDerecha(2015,3) devolverá 0
def extraerDigitoDesdeDerecha(numero, posicion):
   assert type(numero) and type(posicion) == int
   posicion -= 1
   return ((numero//(10**posicion))%10)

def contarDigitos(numero, digitos):
   assert type(numero) and type(digitos) == int
   if numero == 0:
      return 0
   elif numero//10 == 0:
      return digitos+1
   else:
      return contarDigitos(numero//10, digitos+1)

def sumaMultiplicacionDigitos(rut, suma, aux, serie):
   assert type(rut) and type(suma) and type(aux) and type(serie) == int
   if aux==contarDigitos(rut,0):
      return suma
   else:
         if serie==8:
            serie = 2
         suma += extraerDigitoDesdeDerecha(rut, aux+1)*serie
         return sumaMultiplicacionDigitos(rut, suma, aux+1, serie+1)

def digitoVerificador(rut):
   suma = sumaMultiplicacionDigitos(rut, 0, 0, 2)
   resto = suma % 11
   verificador = 11 - resto
   if verificador == 11: return str(0)
   elif verificador == 10: return "K"
   else: return str(verificador)

def consultaDigitoVerificador():
   rut = int(input("Ingrese el rut: \n"))
   if rut != 0:
      print ("El RUT ingresado es: " + str(rut))
      print (u"El dígito verificador es: " + digitoVerificador(rut)) # Prefiero que se vea feo a no usar tilde jajajaj

consultaDigitoVerificador()
