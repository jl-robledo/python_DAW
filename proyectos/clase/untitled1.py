# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 13:44:41 2021

@author: DAW
"""

# NUMEROS DIVISIBLES POR 3 

numeros = [121,155,123,13,14,15,21]

divisiblepor3 = [valor for valor in numeros if valor % 3 == 0]
div3lambda = list(filter(lambda x : x%3==0, numeros))

print(divisiblepor3)
print(div3lambda)



# funcion que devuelve el inverso de un numero

def funcion(x):
    return 1/x

inv= lambda x : 1/x

lista2= [1,2,3,4,5]

#mostrar el inverso
print([funcion(index) for index in lista2])
print([inv(elemento) for elemento in lista2])

l1= [1,2,3]
l2= [4,5,6]
l= [(1,2),(1,3),(1,4),(1,5)]

comprension = lambda l: [x for x in l]
print (comprension)