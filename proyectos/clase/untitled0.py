# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 00:57:13 2020

@author: DAW
"""

"""

Realizar un porgrama que calcule la suma de las areas de las estancias de una 
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

# funciones que se van a utilizar

# funcion para tomar datos de las hhabitaciones
def datos ():
    ancho = int (input("Introduce el ancho de la habitacion: "))
    largo = int (input("Introduce el largo de la habitacion: "))
    return (ancho, largo)

# funcion para calcular el area de las habitaciones
def area (tupla):
    return tupla[0]*tupla[1]

# funcion para saber que estancia es mayor de 10 metros
def diez (area):
    return (area > 10)


# programa 

estancias = int(input("Introduce el numero de estancias de la casa: "))

# Creamos una lista vacia para guardar los datos de las estancias
listaEstancias = []

# Introduccion de los datos de las estancias y guardamos en una lista
for i in range (0 , estancias):
    listaEstancias += [datos()]
       
# comprobacion de que se han introducido bien los datos de las estancias
print ("Datos introducidos: ")
print (listaEstancias)

# lista de Areas de las estancias
print ("Area de las estancias: ")
print (list(map(area, listaEstancias)))


# suma de todas las areas 
print ("Area total: ")
print(sum(list(map(area, listaEstancias))))


# Que solo salgan las areas mayores de 10 metros
# hay que guardar los datos de la lista de areas
listaAreas = (list(map(area, listaEstancias)))
print ("Areas mayores a 10 metros: ")
print(list(filter(diez, listaAreas)))

