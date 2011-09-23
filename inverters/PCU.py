import matplotlib.pyplot as plt   # version 1.0.1
import numpy as np                # version 1.5.1

Vbattery = [48.12, 48.02, 48.7, 48.7, 48.1, 48.1, 48.9, 48.1, 48.05, 47.89, 48.86, 48.9, 49.19, 51.52, 54.2]
Ibattery = [6.8, 7.7, 5.8, 5.5, 4.8, 3.4, 3.6, 3.5, 4.1, 6.9, 4.9, 8.7, 2.9, 2.1, 2.5]
VA = [Vbattery[x]*Ibattery[x] for x in range(len(Vbattery))]
print VA
Wmains = [177.6, 221.5, 138.6, 126.1, 98.8, 38.9, 43.1, 37.3, 66.2, 189.3, 108.4, 269.8, 0, 0, 0]

fig = plt.figure()
ax = fig.add_axes((.1,.3,.8,.6))
ax.plot(VA, Wmains, 'x', c='r', ms=10)
ax.plot(VA, VA, '-', lw=3, c='0.85')
ax.set_xlim((0,450))
ax.set_xlabel("power entering PCU")
ax.set_ylabel("power leaving PCU")
ax.grid(True)
ax.set_title("PCU efficiency")
fig.savefig('PCUefficiency.pdf')

fig1 = plt.figure()
ax1 = fig1.add_axes((.1,.3,.8,.6))
ax1.plot(Wmains, [Wmains[x]/VA[x] for x in range(len(VA))], 'o', c='r', ms=10)
#ax1.plot(VA, VA, '-', lw=3, c='0.85')
#ax1.set_xlim((0,450))
ax1.set_xlabel("power load")
ax1.set_ylabel("PCU efficiency")
ax1.grid(True)
ax1.set_title("PCU efficiency")
fig1.savefig('PCUefficiencyPercent.pdf')
