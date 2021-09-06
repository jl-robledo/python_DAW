# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 09:47:54 2021

@author: David Calvo
@author: Jose Luis Robledo
"""
import random

def datosAlumnos():
    print ("David Calvo")
    print ("Jose Luis Robledo")

#Funcion para mostrar la lista de los numeros, le pasamos por parametros los numeros y estrellas posibles.
def mostrarBoleto(listaNumeros, listaEstrellas):
    print("--------------------")
    print("-------NUMEROS------")
    print(f"| {listaNumeros[0]} {listaNumeros[9]} {listaNumeros[18]} {listaNumeros[27]} {listaNumeros[36]} {listaNumeros[45]} |")
    print(f"| {listaNumeros[1]} {listaNumeros[10]} {listaNumeros[19]} {listaNumeros[28]} {listaNumeros[37]} {listaNumeros[46]} |")
    print(f"| {listaNumeros[2]} {listaNumeros[11]} {listaNumeros[20]} {listaNumeros[29]} {listaNumeros[38]} {listaNumeros[47]} |")
    print(f"| {listaNumeros[3]} {listaNumeros[12]} {listaNumeros[21]} {listaNumeros[30]} {listaNumeros[39]} {listaNumeros[48]} |")
    print(f"| {listaNumeros[4]} {listaNumeros[13]} {listaNumeros[22]} {listaNumeros[31]} {listaNumeros[40]} {listaNumeros[49]} |")
    print(f"| {listaNumeros[5]} {listaNumeros[14]} {listaNumeros[23]} {listaNumeros[32]} {listaNumeros[41]}    |")
    print(f"| {listaNumeros[6]} {listaNumeros[15]} {listaNumeros[24]} {listaNumeros[33]} {listaNumeros[42]}    |")
    print(f"| {listaNumeros[7]} {listaNumeros[16]} {listaNumeros[25]} {listaNumeros[34]} {listaNumeros[43]}    |")
    print(f"| {listaNumeros[8]} {listaNumeros[17]} {listaNumeros[26]} {listaNumeros[35]} {listaNumeros[44]}    |")
    print("--------------------")
    print("-----ESTRELLAS------")
    print(f"|     {listaEstrellas[0]}  {listaEstrellas[4]}  {listaEstrellas[8]}      |")
    print(f"|     {listaEstrellas[1]}  {listaEstrellas[5]}  {listaEstrellas[9]}     |")
    print(f"|     {listaEstrellas[2]}  {listaEstrellas[6]}  {listaEstrellas[10]}     |")
    print(f"|     {listaEstrellas[3]}  {listaEstrellas[7]}  {listaEstrellas[11]}     |")
    print("--------------------")

#Funcion para elegir los numeros con los que vas a jugar, le pasamos por parametros la lista de los numeros posibles y la lista de la combinacion elegida
def crearBoletoNumero(listaNumeros, combinacionElegidaNumeros):
    i=1
    while i <=5:
        entrada=int(input(f"Introduce el Numero {i}: "))
        if(entrada in range(1, 51)):
            # comprobamos que no se ha introducido ese numero
            if(listaNumeros[entrada-1]!="X") and (listaNumeros[entrada-1]!="X "):
                if (entrada<10) :
                    listaNumeros[entrada-1]="X"
                    combinacionElegidaNumeros+=[entrada]
                    i=i+1
                else:
                    listaNumeros[entrada-1]="X "
                    combinacionElegidaNumeros+=[entrada]
                    i=i+1
            else:
                print("Numero ya introducido")
        else:
            print("El numero no es válido")

#Funcion para elegir las estrellas con las que vas a jugar, le pasamos por parametros la listade los estrellas posibles y la lista de la combinacion elegida             
def crearBoletoEstrellas(listaEstrellas, combinacionElegidaEstrellas):
    i=1
    while i <=2:
        entrada=int(input(f"Introduce la Estrella {i}: "))
        if(entrada in range(1, 13)):
            # comprobamos que no se ha introducido ese numero
            if(listaEstrellas[entrada-1]!="X") and (listaEstrellas[entrada-1]!="X "):
                if (entrada<10):
                    listaEstrellas[entrada-1]="X"
                    combinacionElegidaEstrellas+=[entrada]
                    i=i+1
                else:
                    listaEstrellas[entrada-1]="X "
                    combinacionElegidaEstrellas+=[entrada]
                    i=i+1
            else:
                print("Estrella ya introducido")
        else:
            print("La estrella no es válida")
    
#Funcion para generar las conbinaciones ganadoras
def generarSorteo(combinacionGanadoraNumeros, combinacionGanadoraEstrellas):
    
    i=1
    while i<=5:
        if i not in combinacionGanadoraNumeros:
            # Llenado de la lista de los numeros con la funcion random.randint entre el 1 y el 12 incluidos
            combinacionGanadoraNumeros += [random.randint (1 , 50)]
            i = i + 1
    i=1
    while i<=2:
        if i not in combinacionGanadoraEstrellas:
            # Llenado de la lista de las estrellas con la funcion random.randint entre el 1 y el 12 incluidos
            combinacionGanadoraEstrellas += [random.randint (1 , 12)]
            i = i + 1

    # ordenamos los numeros para que sean mas legibles
    combinacionGanadoraNumeros.sort()
    print("--------------------")
    print ("Combinacion ganadora NUMEROS: ")
    print (combinacionGanadoraNumeros)

    # ordenamos las estrellas para que sean mas legibles
    combinacionGanadoraEstrellas.sort()
    print("--------------------")
    print ("Combinacion ganadora ESTRELLAS: ")
    print (combinacionGanadoraEstrellas)

#Funcion para comprobar si el boleto esta premiado, le pasamos por parametros las listas de numeros y estrellas elegidas y las listas de numeros y estrellas ganadoras.
def comprobarPremio(combinacionElegidaNumeros, combinacionElegidaEstrellas, combinacionGanadoraNumeros, combinacionGanadoraEstrellas):
    numerosAcertados=0
    estrellasAcertadas=0
    premios=["15000000 €", "3000000 €", "1500000 €", "800000 €", " 500000 €", "350000 €", 
           "320000 €", "300000 €", "150000 €", "50000 €", "10000 €", "60 €"]
    
    # comprobamos los numeros elegidos si estan en la combinacion ganadora, en caso de encontrarse se suma 1 al contador.
    for i in range(0,5):
        if combinacionElegidaNumeros[i] in combinacionGanadoraNumeros:
            numerosAcertados=numerosAcertados+1
    
    # comprobamos las estrellas elegidas si estan en la combinacion ganadora, en caso de encontrarse se suma 1 al contador.
    for i in range(0,2):
        if combinacionElegidaEstrellas[i] in combinacionGanadoraEstrellas:
            estrellasAcertadas=estrellasAcertadas+1
            
    # con los resultados obtenidos de los contadores de aciertos, comprobamos los premios.
    if numerosAcertados==5 and estrellasAcertadas==2:
        print('Enhorabuena, tu premio es de ' + premios[0])
        
    elif numerosAcertados==5 and estrellasAcertadas==1:
        print('Enhorabuena, tu premio es de ' + premios[1])
    
    elif numerosAcertados==5 and estrellasAcertadas==0:
        print('Enhorabuena, tu premio es de ' + premios[2])
    
    elif numerosAcertados==4 and estrellasAcertadas==2:
        print('Enhorabuena, tu premio es de ' + premios[3])
        
    elif numerosAcertados==4 and estrellasAcertadas==1:
        print('Enhorabuena, tu premio es de ' + premios[4])
        
    elif numerosAcertados==4 and estrellasAcertadas==0:
        print('Enhorabuena, tu premio es de ' + premios[5])
        
    elif numerosAcertados==3 and estrellasAcertadas==2:
        print('Enhorabuena, tu premio es de ' + premios[6])
        
    elif numerosAcertados==3 and estrellasAcertadas==1:
        print('Enhorabuena, tu premio es de ' + premios[7])
        
    elif numerosAcertados==3 and estrellasAcertadas==0:
        print('Enhorabuena, tu premio es de ' + premios[8])
        
    elif numerosAcertados==2 and estrellasAcertadas==2:
        print('Enhorabuena, tu premio es de ' + premios[9])
        
    elif numerosAcertados==2 and estrellasAcertadas==1:
        print('Enhorabuena, tu premio es de ' + premios[10])
        
    elif numerosAcertados==2 and estrellasAcertadas==0:
        print('Enhorabuena, tu premio es de ' + premios[11])
        
    else:
        print('No premiado. Nunca pierda la esperanza...')
        