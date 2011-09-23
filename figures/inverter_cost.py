'''
script to create chart of inverter power vs cost per watt
'''

from __future__ import division
import matplotlib.pyplot as plt
import numpy as np

def addEntry(key, cost, power):
    dict[key] = {}
    dict[key]['cost'] = cost
    dict[key]['power'] = power
    dict[key]['cost_per_watt'] = dict[key]['cost'] / dict[key]['power']

dict = {}

addEntry('morning star',  cost=200, power=300)
addEntry('tripp lite',    cost=70,  power=375)
addEntry('victron', cost =150,  power =350)

fig = plt.figure()
axes = fig.add_axes((0.1, 0.1, 0.8, 0.8))
keys = dict.keys()


for key in dict.keys():
    axes.plot(dict[key]['power'], dict[key]['cost_per_watt'], 'ko')
    axes.text(dict[key]['power'], dict[key]['cost_per_watt'], key)


axes.set_ylabel('Cost per Watt (USD)')
axes.set_xlabel('Power')
plt.grid(ls='-', color='#dddddd')

fig.savefig('plots/inverter_cost.pdf')

plt.close()
