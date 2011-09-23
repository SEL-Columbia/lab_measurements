from __future__ import division
import matplotlib.pyplot as plt
import numpy as np

def addEntry(key, cost, energy, rank):
    dict[key] = {}
    dict[key]['cost'] = cost
    dict[key]['energy'] = energy
    dict[key]['cpkWh'] = dict[key]['cost'] / dict[key]['energy']
    dict[key]['rank'] = rank

dict = {}

addEntry('Cell Phone Charge',  cost = 0.25, energy = 0.005,  rank=2)
addEntry('D Cell',             cost = 0.30, energy = 0.0022, rank=3)
addEntry('Car Battery Charge', cost = 1.0,  energy = 0.12,   rank=1)
addEntry('SharedSolar',        cost = 1.0,  energy = 0.2,    rank=0)
#addEntry('Grid Mali',   cost = 16,   energy = 16/0.2, rank=4)

fig = plt.figure()
axes = fig.add_axes((0.3, 0.5, 0.6, 0.4))

keys = dict.keys()
numKeys = len(dict.keys())

tick_labels = ['','','','','']

for key in dict.keys():
    axes.semilogx(dict[key]['cpkWh'], dict[key]['rank'], 'ko')
    tick_labels[dict[key]['rank']] = key



axes.set_xlabel('Cost per kWh (USD)')
axes.set_ylabel('')
axes.set_title('Unit Cost of Energy')
axes.set_yticks(range(numKeys))
axes.set_ylim((-0.5, numKeys - 0.5))
axes.set_yticklabels(tick_labels)
plt.grid(ls='-', color='#dddddd')
#plt.show()

fig.savefig('cost_per_kWh.pdf')

plt.close()