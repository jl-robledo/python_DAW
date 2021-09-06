# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 09:47:21 2021

@author: David Calvo
@author: Jose Luis Robledo
"""

import euromillon_funciones

#Se genera la lista de numeros
listaNumeros=[]
for i in range(1, 51):   
    listaNumeros += [i]

#Se genera la lista de estrellas
listaEstrellas=[]
for i in range(1, 13):
    listaEstrellas += [i]


# creamos las listas que necesitamos para los numeros y para las estrellas
combinacionElegidaNumeros=[]
combinacionElegidaEstrellas=[]


#creamos las listas de los numeros y estrellas que han salido en el sorteo
combinacionGanadoraNumeros=[]
combinacionGanadoraEstrellas=[]

#mostramos los datos de los alumnos
euromillon_funciones.datosAlumnos()

# mostramos la lista de los numeros y estrellas que podemos elegir    
euromillon_funciones.mostrarBoleto(listaNumeros, listaEstrellas)


#creamos el boleto con los numeros y estrellas que se introduzcan por el usuario
euromillon_funciones.crearBoletoNumero(listaNumeros, combinacionElegidaNumeros)
euromillon_funciones.crearBoletoEstrellas(listaEstrellas, combinacionElegidaEstrellas)

#mostramos el boleto elegido por el usuario
euromillon_funciones.mostrarBoleto(listaNumeros, listaEstrellas)

#mostramos la combinacion elegida por el usuario
euromillon_funciones.mostrarBoleto(combinacionElegidaNumeros, combinacionElegidaEstrellas)

# se hace el sorteo con los numeros y estrellas
euromillon_funciones.generarSorteo(combinacionGanadoraNumeros, combinacionGanadoraEstrellas)

#comprobamos el los numeros y estrellas que se han acertado
euromillon_funciones.comprobarPremio(combinacionElegidaNumeros, combinacionElegidaEstrellas, combinacionGanadoraNumeros, combinacionGanadoraEstrellas)




