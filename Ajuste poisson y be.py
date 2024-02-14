# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 10:29:35 2024

@author: Publico
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.stats import poisson
import scipy as sp
from scipy.optimize import curve_fit

# # axes:
mpl.rcParams['axes.xmargin'] = 0
mpl.rcParams['axes.grid'] = True
mpl.rcParams['axes.grid.axis'] = 'both'
mpl.rcParams['axes.axisbelow'] = True

# # figure:
mpl.rcParams['figure.autolayout'] = True
mpl.rcParams['figure.dpi'] = 100

# def poisson(x,k):
#     return np.exp(-k)*(k**x)/sp.special.factorial(x)

fotones = np.loadtxt('Mediciones/laser estable 1microsegundo.txt')

fig, ax = plt.subplots()

maximo = int(max(fotones))

# n, bins, patches = ax.hist(fotones, bins=np.arange(0,maximo+1), density=True, align='left')
n, bins = np.histogram(fotones, bins=np.arange(0,maximo+1), density=True)
ax.bar(bins[:-1], n, width=1, ec='k', label='Datos', color='gray', alpha=0.5)

p = int(np.mean(fotones))
print(p)
y = poisson(p)
#x = poisson(p+1)

ax.plot(bins[:-1], n, '.', color='k')
ax.plot(bins[:-1], y.pmf(bins[:-1]), '.-', color='r', label=f'Poisson m = {p}')
#ax.plot(bins[:-1], x.pmf(bins[:-1]), '.-', color='b', label=f'Poisson m = {p+1}')
ax.set_ylabel('Probabilidad')
ax.set_xlabel('Cantidad de fotones')
ax.legend()
plt.show()
#%%

# get random numbers that are poisson deviated
#data_set = np.random.poisson(4, 2000)

# the bins have to be kept as a positive integer because poisson is a positive integer distribution
bins = np.arange(42) - 0.5
entries, bin_edges, patches = plt.hist(fotones, bins=bins, density=True, label="Medición")

# calculate bin centers
middles_bins = (bin_edges[1:] + bin_edges[:-1]) * 0.5


def fit_function(k, lamb):
    # The parameter lamb will be used as the fit parameter
    return poisson.pmf(k, lamb)


# fit with curve_fit
parameters, cov_matrix = curve_fit(fit_function, middles_bins, entries)

# plot poisson-deviation with fitted parameter
x_plot = np.arange(0, 41)

plt.plot(
    x_plot,
    fit_function(x_plot, *parameters),
    marker="D",
    linestyle="-",
    color="black",
    label="Ajuste",
)
plt.legend()
plt.show()
#%%
fotones_be=np.loadtxt('Mediciones/conteoT5nsmaschicaquetc3.txt')
bins = np.arange(5) - 0.5
entries, bin_edges, patches =plt.hist(fotones_be,bins=bins,density=True,label="Medición")
def bose_einstein(k,m):
    return (m**(k))/((1+m)**(1+k))
middles_bins = (bin_edges[1:] + bin_edges[:-1]) * 0.5
parameters, cov_matrix = curve_fit(bose_einstein, middles_bins, entries)
print(parameters)
x_plot = np.arange(0, 4)


plt.plot(
    x_plot,
    bose_einstein(x_plot, *parameters),
    marker="D",
    linestyle="-",
    color="black",
    label="Ajuste",
)
plt.legend()
plt.show()