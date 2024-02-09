# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:09:26 2024

@author: Publico
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def poisson(x,L):
    p=np.exp(-L)*L**x/np.math.factorial(x)
    return p
fotones=np.loadtxt('laserestable.txt')
plt.figure()
maximo=int(max(fotones))
n,bins,patches=plt.hist(fotones,bins=np.linspace(0,maximo,maximo+1), align='left')
bins0=np.delete(bins,len(bins)-1)
bins1=bins0+0.5
plt.plot(bins1,n,'.-')
plt.show()