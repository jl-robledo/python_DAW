# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 12:47:34 2020

@author: Jose Luis Robledo
"""


print ("Numeros del 1 al 5 con for")
for i in range(1,6):
    print (i, end=" ")


print()
print ("Numeros del 1 al 5 con while")
i=1
while i<=5:
    print(i, end=" ")
    i += 1

print()  
j = range (0, 101)
while i <=(len(j)-1):
    for i in j:
        if i%5==0:
            print (i, end=" ")
            i+=1