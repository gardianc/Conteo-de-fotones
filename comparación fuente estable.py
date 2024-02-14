import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
import sklearn
from sklearn.feature_selection import chi2


# axes:
mpl.rcParams['axes.xmargin'] = 0
mpl.rcParams['axes.grid'] = True
mpl.rcParams['axes.grid.axis'] = 'both'
mpl.rcParams['axes.axisbelow'] = True

# figure:
mpl.rcParams['figure.autolayout'] = True
mpl.rcParams['figure.dpi'] = 100

# def poisson(x,k):
#     return np.exp(-k)*(k**x)/sp.special.factorial(x)

fotones = np.loadtxt('Mediciones/laser estable 1microsegundo.txt')

fig, ax = plt.subplots()

maximo = int(max(fotones))

# n, bins, patches = ax.hist(fotones, bins=np.arange(0,maximo+1), align='left', density=True)
n, bins = np.histogram(fotones, bins=np.arange(0,maximo+1), density=True)
ax.bar(bins[:-1], n, width=1, ec='k', label='Datos', color='gray', alpha=0.5)

p = np.mean(fotones)
print(f'Media: {p}\nVarianza={np.var(fotones)}')

# puntos = np.array(list(bins) + [i for i in range(42, 100)])
# n_ext = np.array(list(n) + [0 for i in range(41, 100)])
# print(puntos)

y = stats.poisson.pmf(bins[:-1], p)


res_ks = stats.kstest(n, stats.poisson.pmf(bins[:-1], p))
print(res_ks[0], res_ks[1])

ax.plot(bins[:-1], n, '.', color='k')
ax.plot(bins[:-1], y, '.-', color='r', label=f'Poisson m = {p}')
# ax.plot(bins[:-1], x.pmf(bins[:-1]), '.-', color='b', label=f'Poisson m = {int(p)}')
ax.set_ylabel('Probabilidad')
ax.set_xlabel('Cantidad de fotones')
ax.legend()
# plt.savefig('Gráficos/laser estable 500nanosegundos.pdf', format='pdf', dpi=150)
plt.show()
