import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import signal
import pyvisa
import osciloscope as osc
rm = pyvisa.ResourceManager()
osc = osc.Osciloscope()
umbral=0.0008224448897795593
N = 1000
fotones=[]
plt.figure(), plt.clf()
#fig, [ax1, ax2] = plt.subplots(1, 2)
for n in range(N):
    tiempo, data0 = osc.getWindow(1)
    data=data0*(-1)
    i_picos , dicc =sp.signal.find_peaks(data, height=umbral,distance=30)
    # tiempo_picos=tiempo[i_picos]
    # alturas = dicc['peak_heights']
    # alturas0=alturas*(-1)
    numdepicos=len(i_picos)
    fotones.append(numdepicos)
    # maximo=int(max(fotones))
    # ax1.cla()
    print(f'N= {n}', f'cantidad de fotones= {numdepicos}')
    # ax1.plot(tiempo, data0,'.-')
    # ax1.plot(tiempo_picos, alturas0, 'o')
    # ax2.hist(fotones,bins=np.linspace(0,maximo,maximo+1))
    # plt.pause(0.1) 
np.savetxt('laserestable.txt', fotones)
maximo=int(max(fotones))
plt.hist(fotones,bins=np.linspace(0,maximo,maximo+1))