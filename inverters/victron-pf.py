import matplotlib.pyplot as plt
import numpy as np

res = [10000, 5000, 2500, 1000, 500]
loads = [(np.square(240.0)/res[x]) for x in range(len(res))]
loads = [0] + loads
voltage = 48.0
current = [0.25, 0.36, 0.47, 0.7, 1.37, 2.56]
power = [(current[x]*voltage) for x in range(len(current))]

fig1 = plt.figure()
ax1 = fig1.add_axes((.1, .3, .8, .6))
#ax1.plot(loads, power, 'x-', label='total power consumed')
#ax1.plot(loads, loads, '-', c='0.5', lw=3, label='loads')
ax1.plot(loads, [(loads[x]/power[x]) for x in range(len(power))], 'o-', label='pf = 1.0')
ax1.plot(20, .41, 'x', ms=10, label='pf = 0.44')
ax1.plot(44, .636, 'x', ms=10, label='pf = 0.38')
ax1.legend(loc=0)
ax1.set_xlabel("load (watts)")
ax1.set_ylabel("efficiency")
ax1.grid(True)
ax1.set_title("victron inverter efficiency vs. load power, for 3 power factors")
fig1.savefig('plots/victron-powerfactor.pdf')
