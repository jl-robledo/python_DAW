# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 08:41:27 2021

@author: Jose Luis Robledo
"""

import pandas as pd
listaJugadores=["Pepe", "Juan", "Luis"]
listaIndices=[1, 5, 23]
serie = pd.Series(listaJugadores, index=listaIndices)

print(*serie)