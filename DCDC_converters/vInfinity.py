import matplotlib.pyplot as plt   # version 1.0.1
import numpy as np                # version 1.5.1

converters = [5, 12]
res = [[5.35, 2.64, 1.83, 1.42],[30.45, 15.22, 10.23, 7.72]]
loads = [[],[]]
for i in range(len(res)):
    loads[i] = [(np.square(converters[i])/res[i][x]) for x in range(len(res[i]))]
    loads[i] = [0] + loads[i]
voltage = 48.0
current = [[0, 0.115, 0.23, 0.34, 0.45],[0, .11, .21, .32, .43]]
power = [[],[]]
for y in range(len(current)):
    power[y] = [(current[y][x]*voltage) for x in range(len(current[y]))]
print power
fig = plt.figure()
ax = fig.add_axes((.1, .3, .8, .6))
#ax.plot(loads, power, 'x-', label='total power consumed')
#ax.plot(loads, loads, '-', c='0.5', lw=3, label='loads')
eff=np.zeros((2,len(power[0])))
for x in range(len(power)):
    for y in range(len(power[0])):
        if y == 0:
            eff[x][y]=1
        else:
            eff[x][y] = loads[x][y]/power[x][y]
print eff
for i in range(len(res)):
    ax.plot(loads[i], eff[i], 'o-', label=str(converters[i]))
ax.legend(loc=0)
ax.set_xlabel("load (watts)")
ax.set_ylabel("efficiency (watts/watts)")
ax.set_title("DC-DC (48v to 5/12v) converter power consumed vs. load power")
ax.set_ylim((-0.1,1.1))
fig.savefig('vInfinity.pdf')
