import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.stats import poisson
import scipy as sp

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

fotones = np.loadtxt('Mediciones/laserestable.txt')

fig, ax = plt.subplots()

maximo = int(max(fotones))

# n, bins, patches = ax.hist(fotones, bins=np.arange(0,maximo+1), density=True, align='left')
n, bins = np.histogram(fotones, bins=np.arange(0,maximo+1), density=True)
ax.bar(bins[:-1], n, width=1, ec='k', label='Datos', color='gray', alpha=0.5)

p = int(np.mean(fotones))+1
print(p)
y = poisson(p)
x = poisson(p-1)

ax.plot(bins[:-1], n, '.', color='k')
ax.plot(bins[:-1], y.pmf(bins[:-1]), '.-', color='r', label='Poisson m = 13')
ax.plot(bins[:-1], x.pmf(bins[:-1]), '.-', color='b', label='Poisson m = 12')
ax.set_ylabel('Probabilidad')
ax.set_xlabel('Cantidad de fotones')
ax.legend()
plt.show()