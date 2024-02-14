import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import signal
import matplotlib as mpl

# axes:
mpl.rcParams['axes.xmargin'] = 0
mpl.rcParams['axes.grid'] = True
mpl.rcParams['axes.grid.axis'] = 'both'
mpl.rcParams['axes.axisbelow'] = True

# figure:
mpl.rcParams['figure.figsize'] = [7.4, 4.8]
mpl.rcParams['figure.autolayout'] = True
mpl.rcParams['figure.dpi'] = 100

# fontsizes
mpl.rcParams['xtick.labelsize'] = 12
mpl.rcParams['ytick.labelsize'] = 12
mpl.rcParams['legend.fontsize'] = 12
mpl.rcParams['legend.title_fontsize'] = 12
mpl.rcParams['axes.labelsize'] = 16

# save
mpl.rcParams['savefig.bbox'] = 'tight'

# cargo los datos
data = np.loadtxt('Mediciones/50ms data.csv', delimiter=',')*1e3
tiempo = np.loadtxt('Mediciones/50ms tiempo.csv', delimiter=',')

umbral=0.0008224448897795593*1e3

data=data*(-1)
i_picos , dicc =signal.find_peaks(data, height=umbral,distance=30)
tiempo_picos=tiempo[i_picos]
alturas = dicc['peak_heights']
alturas0=alturas*(-1)

fig, ax = plt.subplots()
ax.plot(tiempo, data*(-1),'.-', color='gray', label='Señal')
ax.axhline(-umbral, color='r', linestyle='--', label='Umbral')
ax.plot(tiempo_picos, alturas0, 'o', color='k', label='Fotocuentas')
ax.set_ylabel('Voltaje [mV]')
ax.set_xlabel('Tiempo [s]')
ax.legend()
plt.savefig('Gráficos/pantallaTgrande.pdf', format='pdf', dpi=150)
plt.show()