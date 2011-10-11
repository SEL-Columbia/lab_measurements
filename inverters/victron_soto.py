'''
this script plots the data taken by natasha on victron inverter efficiency with
compact fluorescent lightbulb loads on the meter
'''


import matplotlib.pyplot as plt   # version 1.0.1
import numpy as np                # version 1.5.1

d = np.loadtxt('csv/victron_efficiency_pf.csv',skiprows=1,usecols=[0,1,2,4,10],delimiter=',', dtype=float)

# grab columns
dc_voltage = d[:,1]
dc_current = d[:,2]
mains_power = d[:,4]

# derive arrays from results
dc_power = dc_voltage * dc_current

self_consumption = dc_power - mains_power

plt.plot(mains_power, self_consumption, 'kx')
plt.xlim((0,50))
plt.ylim((0,50))
plt.xlabel('AC Power Delivered By Inverter (W)')
plt.ylabel('Difference of DC Power Consumed and AC Power Delivered')
plt.title('Victron Inverter Self-Consumption (Meter and CFL)')
plt.grid(color='#cccccc', linestyle='-')
plt.savefig('plots/victron_self_consumption.pdf')
plt.close()
#plt.show()


plt.plot(mains_power, mains_power/dc_power, 'kx')
plt.xlim((0,50))
plt.ylim((0,1))
plt.xlabel('AC Power Delivered By Inverter (W)')
plt.ylabel('Efficiency (Ratio of AC Power Delivered to DC Power Consumed)')
plt.title('Victron Inverter Efficiency (Meter and CFL)')
plt.grid(color='#cccccc', linestyle='-')
plt.savefig('plots/victron_efficiency.pdf')
plt.close()
#plt.show()
