# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 13:39:19 2024

@author: Publico
"""
import matplotlib.pyplot as plt
import numpy as np
a = [0,0,1,0,1,0,0,0,1,1]
v = [1,0,1,0,1,0,1,0,1,0]
a1 = np.zeros(10)
v1 = np.ones(10)
corr1 = np.correlate(a, v1,mode='full')
print(corr,corr1) 
corr = np.correlate(voltajes-np.mean(voltajes),voltajes-np.mean(voltajes),mode='full')
plt.plot(corr)