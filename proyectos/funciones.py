# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 09:36:53 2020

@author: DAW
"""


import math


def area_circulo (radio):
    return math.pi * radio **2

listaRadioscirculo = [1, 2, 3]

#devuelve el iterador que es convertido a lista
listaAreasCirculo = list(map(area_circulo, listaRadioscirculo))
print(listaAreasCirculo)
                         

    
def area_triangulo(tuplaValor):
    return (tuplaValor[0] * tuplaValor[1])/2

listaBaseAltura=[(2,3), (5,2), (9,4)]
listaAreasTriangulo = list(map(area_triangulo, listaBaseAltura))
print (listaAreasTriangulo)



def perimetroPoliedro(lados):
    return sum(lados)


""" 
    sumLados= 0
    for lado in lados:
        sumLados += lado
    return sumLados
"""

listaPoliedros = [(2, 3, 5, 8, 9), (5, 2, 4), (9, 9, 4, 4)]
areasPoliedrosList = list(map(perimetroPoliedro, listaPoliedros))

#print(listaPoliedros)
print()
print (f"--- Lista de perimetros ---")
print(areasPoliedrosList)