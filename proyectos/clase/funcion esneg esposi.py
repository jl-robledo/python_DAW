# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 12:02:11 2020

@author: DAW
"""

#La funcion verifica si un numero es negativo 
def esneg(numero):
    #DevuelveTrue/False segun sea o no nº negativo
    return (numero < 0)

def esposi(numero):
    return (numero > 0)

lista = [1, -3 , -2, 15, -100]

if (esneg(lista[2])==False):
    print("Positivo")
else:
    print ("Negativo")
    
    
    
#Muestra los numeros negativos de la lista
# la funcion esneg() se llama para comprobar uno a uno, todos los numeros de la lista
print(list(filter(esneg, lista)))

#Para obtener el resultado de aplicar la funcion a cada elemento de la lista 
#Devuelve [true o false, true o false,...]
print(list(map(esneg, lista)))

#Si queremos comprobar qeu todos los elementos filtrados cumplen la condicion, metemos el map
#Importante ver que al map, hay que pasarle la funcion y ademas la lista que, 
# en este caso sera el resultado de filter(esneg, lista)
# [TRUE, TRUE, TRUE]
print(list(map(esneg,filter(esneg, lista))))