# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 13:39:19 2024

@author: Publico
"""
#%%
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp

# rcParams: (esto es sólo para formatear más lindo los gráficos)
# axes:
mpl.rcParams['axes.xmargin'] = 0
mpl.rcParams['axes.grid'] = True
mpl.rcParams['axes.grid.axis'] = 'both'
mpl.rcParams['axes.axisbelow'] = True

# figure:
mpl.rcParams['figure.autolayout'] = True
mpl.rcParams['figure.dpi'] = 100

#%%

tiempo = np.loadtxt('Mediciones/medicioncorrelación tiempos0.csv', delimiter=',')*1e3 # ms
data = np.loadtxt('Mediciones/medicioncorrelación voltajes0.csv', delimiter=',') # V
voltajes = data - np.mean(data)

intervalo_temp = tiempo[-1]-tiempo[-2] # espacio entre dos samples

corr = np.correlate(voltajes-np.mean(voltajes),voltajes-np.mean(voltajes),mode='full')
corr_positivo = corr[2499:] # corto sólo para los positivos

# busco el primer negativo de la función correlación:
cruce = np.nonzero(corr_positivo<=0)[0][0]
tiempo_de_coherencia = intervalo_temp*cruce

print(f'el ancho en samples de la primer campana es: {cruce}\nel tiempo de coherencia (ancho de la campana en segundos) es {tiempo_de_coherencia} ms')

fig, ax = plt.subplots()
ax.axhline(0, color='k')
# ax.plot(np.arange(len(corr_positivo))*intervalo_temp, corr_positivo, color='k')
ax.plot(np.arange(500)*intervalo_temp, corr_positivo[:500], color='k')
ax.plot(tiempo_de_coherencia, corr_positivo[cruce], 'o', color='b', label=f't = {tiempo_de_coherencia}')
ax.set_xlabel('Tiempo [ms]')
ax.set_ylabel('Autocorrelación') # ver si se normaliza o cómo son las unidades
ax.legend()
plt.show()

#%% tc promedio de 100 pantallas del osciloscopio (sin resistencia)

tc_100 = []
N = 100

for n in range(N):
    data = np.loadtxt(f'Mediciones/medicioncorrelación voltajes{n}.csv', delimiter=',') # V
    voltajes = data - np.mean(data)
    corr = np.correlate(voltajes-np.mean(voltajes),voltajes-np.mean(voltajes),mode='full')
    corr_positivo = corr[2499:] # corto sólo para los positivos

    # busco el primer negativo de la función correlación:
    cruce = np.nonzero(corr_positivo<=0)[0][0]
    tc = intervalo_temp*cruce
    tc_100.append(tc)

tc_promedio = np.mean(tc_100)
print(f'el tiempo de coherencia al promediar 100 pantallas es: {tc_promedio} ns')
