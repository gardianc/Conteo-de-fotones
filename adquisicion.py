# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 09:08:01 2024

@author: Publico
"""
import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
import pyvisa
import osciloscope as osc
rm = pyvisa.ResourceManager()
osc = osc.Osciloscope()


N = 500
alturas_estadistica = []

for n in range(N):
    tiempo, data_pos = osc.getWindow(1)
    data = np.array([d for d in data_pos if d<0])*(-1)
    i_picos, dicc = sp.signal.find_peaks(data, height=0)
    alturas = dicc['peak_heights']
    alturas_estadistica.append(alturas)
    print(n)
    

alturas_estadistica = np.concatenate(tuple(alturas_estadistica))
np.savetxt('datos histograma 2mV 250 ns vidrio.txt', alturas_estadistica)

fig, ax = plt.subplots()
ax.hist(alturas_estadistica)

#%%
fig, ax = plt.subplots()


plt.hist(alturas_estadistica, 50)
plt.yscale('log')
#%%
import pandas as pd
alturas_prendido= np.loadtxt('datos histograma 2mV 250 ns vidrio.txt')
alturas_apagado= pd.read_csv("datos histograma de alturas laser apagado.csv",delimiter=',')
plt.hist(alturas_prendido, 50)
plt.hist(alturas_apagado, 50)
#plt.yscale('log')
#%% código anterior

tiempo, data_pos = osc.getWindow(1)
data = np.array([d for d in data_pos if d<0])*(-1)

i_picos, dicc = sp.signal.find_peaks(data, height=0)

alturas = dicc['peak_heights']
picos = np.array([tiempo[i] for i in i_picos])


fig, [ax1, ax2] = plt.subplots(1, 2)
ax1.plot(tiempo, data_pos,'.-')
ax1.plot(picos, alturas, '.')

ax2.hist(alturas)




print(f'alto: {min(data)}', f'ancho: {min(tiempo)}')
