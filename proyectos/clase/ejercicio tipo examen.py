# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 12:53:16 2020

@author: DAW
"""

"""

Realizar un porgrama que calcule la sma de las areas de las estancias de una 
vivienda de manera que:
    1.- Nos pregunte por el numero de estancias
    2.- Para cada estancia guarde:
        Largo 
        Ancho
    3.- En una lista almacene las áreas de cada estancia
    4.- Devuelva el total de metros cuadrados de la vivienda (suma de todas las estancias)
    5.- Calcular solo las áreas mayores de 10 metros cuadrados
    
Al inicio del programa vamos a utilizar la funcion del ejercicio 0 para que sea lo primero 
que se ejecute en nuestro programa indicandole los parametros correctos.


"""


# funcion para pedir las medidas
def pedirMedidas():
    largo = int (input("Introduce el largo de la esctancia: "))
    ancho = int (input("Introduce el ancho de la esctancia: "))
    return (largo, ancho)


# funcion para calcular el area
def area(tupla):
    return tupla[0]*tupla[1]

# funcion para ver si es mayor o igual a 10
def diez(numero):
    return (numero > 10)


# se pide el numero de habitaciones
numEstancias = int(input("Introduce el numero de estancias: "))

# creamos las lista de habitaciones
listaHabitaciones = []

#  para meter los datos usamos el for y vamos ejecutando pedirMedidas() por 
# tantas estancias como hayamos introducido y nos lo guarda en la lista
for i in range (0, numEstancias):
    listaHabitaciones += [pedirMedidas()]
    
# sacamos la lista de las habitaciones
print ("Comprueba que los datos introducidos son los correctos. ")
print (listaHabitaciones)


# sacamos por pantalla la lista de areas por habitaciones
print("Areas de las estancias: ")
print (list(map(area,listaHabitaciones)))

# sacamos el area total con la suma de las areas
print("Area total: ")
print(sum(list(map(area,listaHabitaciones))))


# sacar por pantalla solo el area de las estancias que sean mayor de 10
# guardo los datos en una nueva lista
listaAreas = list(map(area, listaHabitaciones))


print("Estancias mayores a 10 metros cuadrados: ")
print(list(filter(diez, listaAreas)))

# otra forma de hacerlo
print(list(map(diez, filter(diez, listaAreas))))


