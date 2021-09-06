# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 14:11:24 2021

@author: DAW
"""

import pandas as pd

# serie = pd.Series(data, index=index)

listaJugadores = ['Pepe','Luis', 'Jaime', 'Richi']
listaIndices = [10,25,3,4]

serie = pd.Series(listaJugadores, index=listaIndices)

print (serie)

