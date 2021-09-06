#Zona para variables y constantes:
    
    
#fin de la zona de variables y constantes

print ("---------- CALCULADORA ----------")
print ("----------SUMA---------" )
num1 = int( input("Introduce un numero: "))
num2 = int (input("introduce un segundo numero: "))
resultado = num1 + num2
print (f"El resultado de la SUMA de {num1} + {num2} = {resultado} ")

print ("---------- ---------- ----------")
print ("----------RESTA---------" )
num1 = int( input("Introduce un numero: "))
num2 = int (input("Introduce un segundo numero: "))
resultado = num1 - num2
print (f"El resultado de la RESTA de {num1} + {num2} = {resultado} ")

print ("---------- ---------- ----------")
print ("----------MULTIPLICACION---------" )
num1 = int( input("Introduce un numero: "))
num2 = int (input("Introduce un segundo numero: "))
resultado = num1 * num2
print (f"El resultado de la MULTIPLICACION de {num1} * {num2} = {resultado} ")

print ("---------- ---------- ----------")
print ("----------DIVISION----------" )
num1 = int( input("Introduce un numero: "))
num2 = int (input("Introduce un segundo numero: "))
resultado = num1 / num2
print (f"El resultado de la DIVISION de {num1} / {num2} = {resultado} ")

print ("---------- ---------- ----------")
print ("----------EXPONENTE---------" )
num1 = int( input("Introduce un numero: "))
num2 = int (input("Introduce un segundo numero: "))
resultado = num1 ** num2
print (f"El resultado del EXPONENTE de {num1} elevado a {num2} = {resultado} ")

print ("---------- ---------- ----------")
print ("----------MODULO DE LA DIVISION ENTERA---------" )
num1 = int( input("Introduce un numero: "))
num2 = int (input("Introduce un segundo numero: "))
resultado = num1 % num2
print (f"El resultado del MODULO DE LA DIVISION ENTERA de {num1} % {num2} = {resultado} ")

print ("---------- ---------- ----------")
print ("----------COCIENTE---------" )
num1 = int( input("Introduce un numero: "))
num2 = int (input("Introduce un segundo numero: "))
resultado = num1 // num2
print (f"El resultado del COCIENTE de {num1} // {num2} = {resultado} ")

print ("---------- ---------- ----------")
print ("----------AREA DEL TRIANGULO---------" )
b = int( input("Introduce la base: "))
h = int (input("Introduce la altura: "))
resultado = (b*h)/2
print (f"El resultado de la AREA DEL TRIANGULO de BASE {b} y ALTURA {h} = {resultado} ")

print ("---------- ---------- ----------")
print ("----------AREA DEL RECTANGULO---------" )
b = int( input("Introduce la base: "))
h = int (input("Introduce la altura: "))
resultado = (b*h)
print (f"El resultado de la AREA DEL RECTANGULO de BASE {b} y ALTURA {h} = {resultado} ")

print ("---------- ---------- ----------")
print ("----------AREA DEL CUADRADO---------" )
lado = int( input("Introduce la base: "))
resultado = lado * lado 
print (f"El resultado de la AREA DEL CUADRADO de LADO {lado} es {resultado} ")

print ("---------- ---------- ----------")
print ("----------AREA DEL CIRCULO---------" )
radio = int( input("Introduce el radio: "))
myPI=3.141592
resultado = myPI*radio**2
print (f"El resultado de la AREA DEL CIRCULO de RADIO {radio} es {resultado} ")

print ("---------- ---------- ----------")
print ("----------LONGITUD DEL CIRCULO---------" )
radio = int( input("Introduce el radio: "))
resultado = 2*myPI*radio
print (f"El resultado de la LONGITUD DEL CIRCULO de RADIO {radio} es {resultado} ")

print ("---------- ---------- ----------")
print ("---------- FIN DEL PROGRAMA ----------")
print ("---------- ---------- ----------")