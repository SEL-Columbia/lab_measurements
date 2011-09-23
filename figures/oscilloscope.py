import matplotlib.pyplot as plt   # version 1.0.1
import numpy as np                # version 1.5.1

import scipy.integrate as sint

d = np.loadtxt('csv/NewFile1.csv',skiprows=2,usecols=[0,1,2],delimiter=',')

t = d[:, 0]
v_divider = 100
v = d[:, 2] * v_divider
Rs = 10 #ohms
i = d[:, 1] / Rs
p = v * i

# integrate power over one full cycle --> find zero-crosspts
e = sint.trapz(p[50:216],t[50:216])
print 'average power is ', e * 60, ' watts'

'''
e = sint.trapz(p[:417],t[:417])
print e * 60
'''
plt.plot(t,i, label='current in amps')
plt.plot(t,v/1000, label='voltage in kV')
plt.plot(t,p, label='power in watts')
plt.plot(t, np.ones(len(t))*e*60, c='k', lw='2', label='average power in watts')
plt.legend(loc=0)
plt.show()
