# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 13:57:45 2021

@author: DAW
"""

# -----  GENERADORES  -----

def generador (inicio, fin, incremento):
    while(inicio <= fin):
        yield inicio # devuelve el valor
        inicio += incremento
        

# recorrer los valores del generador
for valor in generador (0,6,1):
    # muestra los valores uno a uno
    print (valor)
    

# obtener una lista del generador
lista = list(generador(0,8,2))
# muestra los valores en una lista [0,2,4,...]
print(lista)




# generar una lista de numeros pares

def generadorPares (inicio, fin, incremento):
    if (inicio%2!=0):
        inicio += 1
        
    while(inicio <= fin):
       yield inicio
       inicio += incremento
    
""" no vale para nada porque solo funciona si el incremento es 2 """         
print (list(generadorPares(1,20,2)))
