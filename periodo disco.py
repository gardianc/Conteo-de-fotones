import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
import pyvisa
import osciloscope as osc
rm = pyvisa.ResourceManager()
#osc = rm.open_resource('USB0::0x0699::0x0363::C065093::INSTR')

osc = osc.Osciloscope()
tiempo, data = osc.getWindow(2)
plt.plot(tiempo, data,'.-')
i_picos , dicc =sp.signal.find_peaks(data,height=1,distance=20)
tiempo2=tiempo[i_picos]
alturas = dicc['peak_heights']
plt.plot(tiempo2, alturas, 'o', color='r')
print(tiempo2)
periodo1=tiempo2[1]-tiempo2[0]
periodo2=tiempo2[2]-tiempo2[1]
print(periodo1)
print(periodo2)