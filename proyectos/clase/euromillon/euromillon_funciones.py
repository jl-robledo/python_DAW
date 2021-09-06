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


def mostrarBoleto(listaNumeros, listaEstrellas):
    print("--------------------")
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
    print(f"|     {listaEstrellas[0]}  {listaEstrellas[4]}  {listaEstrellas[8]}      |")
    print(f"|     {listaEstrellas[1]}  {listaEstrellas[5]}  {listaEstrellas[9]}     |")
    print(f"|     {listaEstrellas[2]}  {listaEstrellas[6]}  {listaEstrellas[10]}     |")
    print(f"|     {listaEstrellas[3]}  {listaEstrellas[7]}  {listaEstrellas[11]}     |")
    print("--------------------")

def crearBoletoNumero(listaNumeros, combinacionElegidaNumeros):
    i=1
    while i <=5:
        entrada=int(input(f"Introduce el numero {i}: "))
        if(entrada in range(1, 51)):
            if(listaNumeros[entrada-1]!="x"):
                listaNumeros[entrada-1]="x"
                combinacionElegidaNumeros+=[entrada]
                i=i+1
            else:
                print("Numero ya introducido")
        else:
            print("El numero no es válido")
                
def crearBoletoEstrellas(listaEstrellas, combinacionElegidaEstrellas):
    i=1
    while i <=2:
        entrada=int(input(f"Introduce la estrella {i}: "))
        if(entrada in range(1, 13)):
            if(listaEstrellas[entrada-1]!="x"):
                listaEstrellas[entrada-1]="x"
                combinacionElegidaEstrellas+=[entrada]
                i=i+1
            else:
                print("Estrella ya introducido")
        else:
            print("La estrella no es válida")
    

def generarSorteo(combinacionGanadoraNumeros, combinacionGanadoraEstrellas):
    i=1
    while i<=5:
        if i not in combinacionGanadoraNumeros:
            combinacionGanadoraNumeros += [random.randint (1 , 50)]
            i = i + 1
    i=1
    while i<=2:
        if i not in combinacionGanadoraEstrellas:
            combinacionGanadoraEstrellas += [random.randint (1 , 12)]
            i = i + 1

    combinacionGanadoraNumeros.sort()
    print ("Combinacion ganadora Numeros: ")
    print (combinacionGanadoraNumeros)


    combinacionGanadoraEstrellas.sort()
    print ("Combinacion ganadora Estrellas: ")
    print (combinacionGanadoraEstrellas)

def comprobarPremio(combinacionElegidaNumeros, combinacionElegidaEstrellas, combinacionGanadoraNumeros, combinacionGanadoraEstrellas):
    numerosAcertados=0
    estrellasAcertadas=0
    premios=["15000000 €", "3000000 €", "1500000 €", "800000 €", " 500000 €", "350000 €", 
           "320000 €", "300000 €", "150000 €", "50000 €", "10000 €", "60 €"]
    
    for i in range(0,5):
        if combinacionElegidaNumeros[i] in combinacionGanadoraNumeros:
            numerosAcertados=numerosAcertados+1
    
    for i in range(0,2):
        if combinacionElegidaEstrellas[i] in combinacionGanadoraEstrellas:
            estrellasAcertadas=estrellasAcertadas+1
    
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
        print('No premiado')
        
        
        
        
        
        
        
        
        
        
        