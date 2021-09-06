# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 08:42:48 2021

@author: Jose Luis Robledo


Comprensión de listas

Es un tipo de construcción que consta de una expresión que determina cómo 
modificar los elementos de una lista, seguida de una o varias clausulas for y, 
opcionalmente, una o varias clausulas if. 
El resultado que se obtiene es una lista.


"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Cada elemento de la lista se eleva al cubo
cubos = [valor ** 3 for valor in lista]
print('Cubos de 1 a 10:', cubos)



x= (1, 3, 4)
y=1
z=3
variable = lambda x,y,z: x[2] if x[0]==y and x[1]==z else 0
print(variable(x,y,z))



numeros = [135, 154, 180, 193, 210]
divisiblespor3 = [valor for valor in numeros if valor % 3.0 == 0] 
div3Lambda = list(filter(lambda x : x%3 == 0, numeros))
print(divisiblespor3)
print(div3Lambda)
    

# Muestra lista con los números divisibles por 3
print(divisiblespor3)  


# Define función devuelve el inverso de un número
def funcion(x):
    return 1/x

inv=lambda x:1/x

lista2 = [1, 2, 3]  # declara lista

# Muestra lista con inversos de cada número
print([funcion(index) for index in lista2])
print([inv(elemento) for elemento in lista2])


resultado = lambda x:[1/x for x in lista2]
print(resultado) 


lis=[1,2,3]

lis2=[4,5,6]

lista=[(1,2), (1,2), (1,2), (1,2)]



comprension = lambda lista: [[x] for x in lista]

print(comprension)