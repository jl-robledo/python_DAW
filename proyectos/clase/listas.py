# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 09:24:38 2020

@author: DAW
"""


#######################################
# lista --> nombre, apellido, edad, vehículos
#vehiculos=["Coche", "Barco", "Moto", "Bus"]
lista=["Andrés", "Chillon", 30, "Coche", "Barco", "Moto", "Bus"]

print(lista)

#modifica el apellido (modificar la posición 1)
nuevoApellido=input("Introduce apellido nuevo: ")
lista[1]=nuevoApellido
print(lista)

nuevaEdad=int(input("Corrige la edad: "))
lista[2]=nuevaEdad
print(lista)


#Añadimos un nuevo elemento
lista+=["hola", "Mundo"]
print(lista)

#Modificamos uno de los elementos de la lista añadiendo contenido
lista[1]+="          "
print(lista.index("hola"))


# Recogemos los datos básicos de la persona menos la edad(posiciones 0 a 2)
print("1.----",lista[0:2])
print("2.----",lista[:2])


# Recogemos los datos de vehículos (posiciones 4 en adelante)
print("3.----",lista[3:])
print("4.----",lista[:])
print("5.----",lista)

#obtención de sublistas
dias=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print(dias[1:4]) #lista con valores 1, 2, 3
print(dias[4:5]) #lista con valor 4
print(dias[4:4]) #lista vacía

print(dias[:4])  #lista hasta el valor 4 (no incluido)
print(dias[4:])  #lista desde el valor 4 (incluido)
print(dias[:])  #lista con todos los valores

#MANIPULACIÓN DE LISTAS
letras=["A","B","C","D","E","F","G","H","I","J","K",]
print(letras)
letras[1:4]=["X","Y"] #sustituimos ["B","C","D"] POR ["X","Y"]
print(letras)
print("       ------")

letras[2:2]=["Z","Z","Z"] #inserta la lista ["Z","Z","Z"] en la posición 2
print(letras)
print("            ------------")
#elimina la sublista correspondiente al rango
letras[0:2]=[]
print(letras)

#Recorrer una lista: recorremos directamente los elementos de la lista
# sólo permite recorrer la lista de principio a fin y utilizar los valores de la lista.
letras=["A","B","C"]
for i in letras:
    print(i, end=" ")

#recorremos la lista a través de sis índices:
# más complicada, permite más flexibilidad
letras=["A","B","C"]
for i in range(len(letras)):
    print(letras[i], end=" ")

#recorrer lista al revés:
letras=["A","B","C"]
for i in range(len(letras)-1, -1, -1):
    print(letras[i], end=" ")
    
#Modificar los elementos de una lista
letras=["A","B","C"]
print(letras)
for i in range(len(letras)):
    letras[i]="X"
    print(letras)    
    
#Eliminar elementos de la lista
    #recorrer la lista al revés.
    #    Si recorremos la lista de principio a fin, al eliminar 
    #    un valor de la lista, la lista se acorta y cuando 
    #    intentamos acceder a los últimos valores se produce 
    #    un error de índice fuera de rango, como muestra el 
    #    siguiente ejemplo en el que se eliminan los valores de 
    #    una lista que valen "B":
            
letras=["A","B","C"]
print(letras)
for i in range(len(letras)-1):
    if(letras[i]=="B"):
        del letras[i]
    print(letras)   

"""
La solución es recorrer la lista en orden inverso, de manera que 
aunque se eliminen elementos y la lista se acorte, los valores 
que todavía no se han recorrido siguen existiendo en la misma 
posición que al principio
"""
letras=["A","B","C"]
print(letras)
for i in range(len(letras)-1, -1, -1):
    if(letras[i]=="B"):
        del letras[i]
    print("Posición",i,"--->", letras) 