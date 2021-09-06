# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 02:23:31 2020

@author: DAW
"""

import functools

def multiplicar (x,y):
    print(x*y)
    return x*y

numero = int(input("De que numero quieres calcular el factorial: "))

lista =range(1, numero+1)
for i in lista:
    print(i , "\n")

valor= functools.reduce(multiplicar, lista)

print("\nResultado de ", numero ,"! = ", valor)

print("\n--------------\n")

lista =[1,2,3,4,5,6,7,8,9,10]

cubos = [valor**3 for valor in lista]
print("Cubos del 1 al 10: ", cubos)


divisible2 = [valor for valor in lista if valor%2==0]
print(divisible2)

def funcion(x):
    return 1/x

print([funcion(i) for i in lista])

# lambda

area_cuadrado = lambda l1,l2 : l1*l2
cuadrados = [(2,2),(3,3),(4,4),(5,5)]
for i in cuadrados:
    lado1 = i[0]
    lado2 = i[1]
    print (area_cuadrado(lado1, lado2))