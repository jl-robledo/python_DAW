# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 13:05:06 2021

@author: DAW
"""



print(" --- CALCULADORA ---")

# definicion de funciones
def suma(num1, num2):
    resultado = (num1+num2)
    return resultado

def resta(num1, num2):
    resultado = (num1-num2)
    return resultado

def multiplicacion(num1, num2):
    resultado = (num1*num2)
    return resultado

def division(num1, num2):
    resultado = (num1/num2)
    return resultado



"""

num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: "))
rSuma = suma(num1, num2)
rResta = resta(num1, num2)
rMultiplicacion = multiplicacion(num1, num2)
rDivision = division(num1, num2)


print("\n\n --- SUMA ---")
print(f"El restultado de la suma de {num1} + {num2} = {rSuma} \n")


print(" --- RESTA ---")
print(f"El restultado de la suma de {num1} - {num2} = {rResta} \n")

print(" --- MULTIPLICACION ---")
print(f"El restultado de la suma de {num1} * {num2} = {rMultiplicacion} \n")

print(" --- DIVISION ---")
print(f"El restultado de la suma de {num1} / {num2} = {rDivision} \n")

"""

# variable para el tipo de operacion que queremos hacer y el texto de la operacion
operacion = 0
texto = ""

print(" --- CALCULADORA --- \n")
print("Que operacion quieres hacer: ")
print(" 1. Sumar")
print(" 2. Restar")
print(" 3. Multiplicar")
print(" 4. Dividir")

operacion = int (input(("Que operacion quieres realizar: ")))
num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: "))

# menu para la calculadora
if operacion == 1:
    resultado = suma (num1, num2)
    texto = "SUMA"

elif operacion == 2:
    resultado = resta (num1,num2)
    texto = "RESTA"

elif operacion == 3:
    resultado = multiplicacion(num1, num2)
    texto = "MULTIPLICACION"
elif operacion == 4:
    resultado = division(num1, num2)
    texto = "DIVISION"
    
else:
    print("Introduce un numero del indice de operaciones")
    

    
print(f"El resultado de la operacion de {texto} de los numeros {num1} y {num2} es {resultado}")




# -----  AREAS DE POLIGONOS CON LAMBDA  ----- #
    
# CUADRADOS

area_cuadrado = lambda x : x*x

listaLadosCuadrados = [1,2,3,4]
listaAreaCuadrados = list(map(area_cuadrado, listaLadosCuadrados))
print ("Area cuadrados: " , listaAreaCuadrados)

# RECTANGULOS

area_rectangulo = lambda b,h : b*h

listaBasesRectangulos = [1,2,3]
listaAlturasRectangulos = [4,5,6]

listaAreaRectangulos = list(map(area_rectangulo, listaBasesRectangulos, listaAlturasRectangulos))
print ("Area rectangulos: " , listaAreaRectangulos)

# TRIANGULOS

area_triangulos = lambda b,h : b*h/2

listaTriangulos = [(1,2),(3,4),(5,6)]
"""
No Funciona:
listaArea_triangulos = list(map(area_triangulos, listaTriangulos))
print ("Area triangulos: ", listaArea_triangulos)

Solo sirve para hacerlo con un for, no se puede hacer con un map
"""
for datos in listaTriangulos:
    base = datos[0]
    altura = datos[1]
    print(area_triangulos(base,altura))
    
    
    
# CIRCULOS

import math
area_circulos = lambda r : r*math.pi

listaRadiosCirculos = [1,2,3,4,5,6,7,8,9]

listaArea_circulos = list(map(area_circulos,listaRadiosCirculos))
print(listaArea_circulos)
    


