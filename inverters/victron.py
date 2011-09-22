import matplotlib.pyplot as plt
import numpy as np

res = [10000, 5000, 2500, 1000, 500]
loads = [(np.square(240.0)/res[x]) for x in range(len(res))]
loads = [0] + loads
voltage = 48.0
current = [0.25, 0.36, 0.47, 0.7, 1.37, 2.56]
power = [(current[x]*voltage) for x in range(len(current))]

fig = plt.figure()
ax = fig.add_axes((.1, .3, .8, .6))
#ax.plot(loads, power, 'x-', label='total power consumed')
#ax.plot(loads, loads, '-', c='0.5', lw=3, label='loads')
ax.plot(loads, [(power[x]-loads[x]) for x in range(len(power))], 'o-', label='inverter consumption')
#ax.legend(loc=0)
ax.set_ylim([0,15])
ax.grid()
ax.set_xlabel("load (watts)")
ax.set_ylabel("power consumed (watts)")
ax.set_title("victron inverter self-consumption with resistive loads")
#plt.show()
fig.savefig('victron.pdf')
