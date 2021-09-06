# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 08:42:07 2021

@author: Jose Luis Robledo
"""

import pandas as pd
spanisP=pd.DataFrame(
        {
                'Nombre':['Casillas','Ramos','Piqué','Pujol','Capdevila','Xavi Alonso0','Busquets','Xabi Hernández','Pedrito','Iniesta','Villa'],
                'Demarcacion':['Portero','Defensa','Defensa','Defensa','Defensa','Medio','Medio','Medio','Delantero','Dios','Delantero'],
                'Equipo':['Real Madrid','Real Madrid','FC. Barcelona','FC. Barcelona','Villareal','Real Madrid','FC. Barcelona','FC. Barcelona','FC. Barcelona','FC. Barcelona','FC. Barcelona']
        
        },columns=['Nombre', 'Demarcacion', 'Equipo']
        ,index=[1,15,3,5,11,14,16,8,18,6,7]     
)

print(  spanisP)

spanisP.loc[10]=['Cesc', 'Delantero', 'Arsenal']

print(  spanisP)