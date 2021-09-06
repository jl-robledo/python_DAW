# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 13:03:37 2020

@author: Jose Luis Robledo
"""

pares, impares = [], []
numeros = range(0,101)

print("----- Numeros del rango -----\n")
for i in numeros:
    print(i,end=" ")
    

for i in numeros:    
    if i%2==0:
        pares+=[i]
    else:
        impares+=[i]

print("\n\n")

print ("----- Lista de numeros PARES -----\n")
for i in pares:
    print (i , end=" ")

print("\n\n")

print ("----- Lista de numeros IMPARES -----\n")
for i in impares:
    print (i, end=" ")
