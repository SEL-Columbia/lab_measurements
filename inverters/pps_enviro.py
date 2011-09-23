import matplotlib.pyplot as plt
import numpy as np

Vbattery = [48.12, 48.02, 48.7, 48.7, 48.1, 48.1, 48.9, 48.1, 48.05, 47.89, 48.86, 48.9, 49.19, 51.52, 54.2]
Ibattery = [6.8, 7.7, 5.8, 5.5, 4.8, 3.4, 3.6, 3.5, 4.1, 6.9, 4.9, 8.7, 2.9, 2.1, 2.5]
Vbattery = np.array(Vbattery)
Ibattery = np.array(Ibattery)

VA = [Vbattery[x]*Ibattery[x] for x in range(len(Vbattery))]
VA = Vbattery * Ibattery

print VA
Wmains = [177.6, 221.5, 138.6, 126.1, 98.8, 38.9, 43.1, 37.3, 66.2, 189.3, 108.4, 269.8, 0, 0, 0]
Wmains = np.array(Wmains)

fig = plt.figure()
ax = fig.add_axes((.1,.3,.8,.6))
ax.plot(VA, Wmains, 'x', c='r', ms=10)
ax.plot(VA, VA, '-', lw=3, c='0.85')
ax.set_xlim((0,450))
ax.set_xlabel("power entering PCU")
ax.set_ylabel("power leaving PCU")
ax.grid(True)
ax.set_title("PCU efficiency")
fig.savefig('plots/PCUefficiency.pdf')
plt.close()

fig = plt.figure()
ax1 = fig.add_axes((.1,.3,.8,.6))
ax1.plot(Wmains, Wmains/VA, 'o', c='r', ms=10)
#ax1.plot(VA, VA, '-', lw=3, c='0.85')
#ax1.set_xlim((0,450))
ax1.set_xlabel("power load")
ax1.set_ylabel("PCU efficiency")
ax1.grid(True)
ax1.set_title("PCU efficiency")
fig.savefig('plots/PCUefficiencyPercent.pdf')

fig2 = plt.figure()
ax1 = fig2.add_axes((.1,.3,.8,.6))
ax1.plot(Wmains, VA - Wmains, 'o', c='r', ms=10)
#ax1.plot(VA, VA, '-', lw=3, c='0.85')
#ax1.set_xlim((0,450))
ax1.set_xlabel("Load (W)")
ax1.set_ylabel("PCU self-consumption (W)")
ax1.set_ylim([0,160])
ax1.grid(True)
ax1.set_title("PPS enviro self consumption")
fig2.savefig('plots/PPS enviro self consumption.pdf')

