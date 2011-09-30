import matplotlib.pyplot as plt   # version 1.0.1
import numpy as np                # version 1.5.1

d = np.loadtxt('csv/victron_efficiency_pf.csv',skiprows=1,usecols=[0,1,2,4,10],delimiter=',', dtype=float)

bulbs = d[:,0]
voltage = d[:,1]
current = d[:,2]
power=[[]]*3
power_mains=[[]]*3
pf_mains=[[]]*3
#need separate arrays for each voltage (48v,52v,56v)
for i in range(len(bulbs)/6):
    numrange = range(6*i,(6*i)+6)
    power[i] = voltage[numrange]*current[numrange]
    power_mains[i] = d[numrange,3]
    pf_mains[i] = d[numrange,4]

fig = plt.figure()
axes = fig.add_subplot(111)
colors=['k','b','g']
for i in range(len(power)):
    axes.plot(power_mains[i], power_mains[i]/power[i], c=colors[i], marker='o', ls='-', label=str(voltage[6*i])+'v')
    #axes.text(cap_kwh[i],cpkwh[i],'  '+model[i],color=color, fontsize=6, ha='left', va='center')
#add power factor data to plot
for j in range(len(power[0])):
    #axes.text(power_mains[len(power)-1][j], (power_mains[len(power)-1][j]/power[len(power)-1][j])-0.05, str(int(bulbs[j]))+' bulbs',color='0.3', fontsize=8, ha='left', va='top')
    axes.text(power_mains[len(power)-1][j], (power_mains[len(power)-1][j]/power[len(power)-1][j])-0.08, ' pf=0.'+str(int(pf_mains[0][j])),color='0.3', fontsize=8, ha='left', va='top')
axes.legend(loc=0)

plt.xlim((0,100))
plt.ylim((-0.1,1.1))

plt.title('Victron Inverter Efficiency with SharedSolar Meter and CFL Bulbs')
plt.xlabel('load: meters + cfl bulbs (W)')
plt.ylabel('efficiency (W/W)')

plt.grid()
plt.savefig('plots/victron_eff_pf.pdf')
plt.show()

plt.close()

