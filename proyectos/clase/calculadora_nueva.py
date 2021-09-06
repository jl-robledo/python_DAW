# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 11:02:13 2021

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