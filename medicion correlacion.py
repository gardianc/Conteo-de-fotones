# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 13:02:18 2024

@author: Publico
"""
import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
import pyvisa
import osciloscope as osc
import pandas as pd
rm = pyvisa.ResourceManager()
#osc = rm.open_resource('USB0::0x0699::0x0363::C065093::INSTR')

osc = osc.Osciloscope()


N = 100
for n in range(N):
    tiempo, voltajes0 = osc.getWindow(1)
    voltajes=voltajes0-4
    #np.savetxt(f'medicioncorrelación tiempos{n}.csv',tiempo,delimiter=',')
    np.savetxt(f'medicioncorrelación voltajes{n}.csv',voltajes,delimiter=',')
    print(n)