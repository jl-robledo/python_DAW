# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 09:47:21 2021

@author: David Calvo
@author: Jose Luis Robledo
"""

import euromillon_funciones

# Se genera la lista de numeros
listaNumeros=[]
for i in range(1, 51):   
    listaNumeros += [i]

# Se genera la lista de estrellas
listaEstrellas=[]
for i in range(1, 13):
    listaEstrellas += [i]

# Creamos las listas que necesitamos para almacenar los numeros y para las estrellas elegidas
combinacionElegidaNumeros=[]
combinacionElegidaEstrellas=[]

# Creamos las listas de los numeros y estrellas que han salido en el sorteo
combinacionGanadoraNumeros=[]
combinacionGanadoraEstrellas=[]


# Mostramos los datos de los alumnos
euromillon_funciones.datosAlumnos()

# Mostramos la lista de los numeros y estrellas que podemos elegir    
euromillon_funciones.mostrarBoleto(listaNumeros, listaEstrellas)

# Creamos el boleto con los numeros y estrellas que se introduzcan por el usuario
euromillon_funciones.crearBoletoNumero(listaNumeros, combinacionElegidaNumeros)
euromillon_funciones.crearBoletoEstrellas(listaEstrellas, combinacionElegidaEstrellas)

# Mostramos la combinacion elegida por el usuario
euromillon_funciones.mostrarBoleto(listaNumeros, listaEstrellas)

# Se hace el sorteo con los numeros y estrellas
euromillon_funciones.generarSorteo(combinacionGanadoraNumeros, combinacionGanadoraEstrellas)

# Comprobamos los numeros y estrellas que se han acertado
euromillon_funciones.comprobarPremio(combinacionElegidaNumeros, combinacionElegidaEstrellas, combinacionGanadoraNumeros, combinacionGanadoraEstrellas)

