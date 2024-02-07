import numpy as np
import matplotlib.pyplot as plt
alturas_prendido= np.loadtxt('datos histograma 2mV 250 ns vidrio.txt')
alturas_apagado= np.loadtxt('datos histograma de alturas laser apagado.csv')
# plt.hist(alturas_prendido, 50)
# plt.hist(alturas_apagado, 50)
N=150
v=np.linspace(0,max(alturas_apagado),N)
fotones_prendido=np.zeros(N-1)
fotones_apagado=np.zeros(N-1)
proporcion=np.zeros(N-1)
for n in range (N-1):
    v_fotones_prendido = np.array([d for d in alturas_prendido if d>v[n]])
    fotones_prendido[n]=len(v_fotones_prendido)
    v_fotones_apagado = np.array([c for c in alturas_apagado if c>v[n]])
    fotones_apagado[n]=len(v_fotones_apagado)
    proporcion[n]=fotones_prendido[n]/fotones_apagado[n]
v1=np.delete(v,N-1)
i_max=np.argmax(proporcion)
umbral=v[i_max]
print(umbral)
plt.plot(v1,proporcion,'o')
plt.show()
# plt.hist(alturas_prendido, N)
# plt.hist(alturas_apagado, N)
# plt.show()