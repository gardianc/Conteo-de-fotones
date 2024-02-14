import numpy as np
import matplotlib.pyplot as plt
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
alturas_prendido = np.loadtxt('Mediciones/datos histograma 2mV 250 ns vidrio.txt')*1e3
errores_prendido = alturas_prendido*0.03
alturas_apagado = np.loadtxt('Mediciones/datos histograma de alturas laser apagado.csv')*1e3
errores_apagado = alturas_apagado*0.03

# plt.hist(alturas_prendido, 50)
# plt.hist(alturas_apagado, 50)

N = 200
v = np.linspace(0,max(alturas_apagado),N)

fotones_prendido = np.zeros(N-1)
fotones_apagado = np.zeros(N-1)
proporcion = np.zeros(N-1)
for n in range (N-1):
    v_fotones_prendido = np.array([d for d in alturas_prendido if d>v[n]])
    fotones_prendido[n] = len(v_fotones_prendido)
    v_fotones_apagado = np.array([c for c in alturas_apagado if c>v[n]])
    fotones_apagado[n] = len(v_fotones_apagado)
    proporcion[n] = fotones_prendido[n]/fotones_apagado[n]
v1 = np.delete(v, N-1)

i_max = np.argmax(proporcion)
umbral = v[i_max]
print(f'El umbral es: ({umbral} +- {v[1]-v[0]}) mV')

fig, ax = plt.subplots()
ax.axvline(v[i_max], linestyle='--', color='r', label='Umbral')
ax.plot(v1, proporcion,'o', color='k', label='Proporción')
ax.set_xlabel('Umbral [mV]')
ax.set_ylabel('Proporción')
ax.legend()
# plt.savefig('Gráficos/prop umbral.pdf', format='pdf', dpi=150)
plt.show()
# plt.hist(alturas_prendido, N)
# plt.hist(alturas_apagado, N)
# plt.show()