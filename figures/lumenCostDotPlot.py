from __future__ import division
import matplotlib.pyplot as plt

def addEntry(key, cost, cpLh, rank):
    dict[key] = {}
    dict[key]['cost'] = cost
    dict[key]['cpLh'] = cpLh
    dict[key]['rank'] = rank

dict = {}

addEntry('Kerosene Lamp',                  cost = 1.20, cpLh = 0.95,  rank=2)
addEntry('D Cell LED Flashlight',     cost = 0.30, cpLh = 6.0,   rank=3)
addEntry('Car Battery With 5W CFL',   cost = 1.0,  cpLh = 0.15,  rank=1)
addEntry('SharedSolar With 5W CFL',   cost = 1.0,  cpLh = 0.125, rank=0)
#addEntry('Grid Mali With CFL',   cost = 16,   cpLh = 16/0.2)

fig = plt.figure()
axes = fig.add_axes((0.3, 0.5, 0.6, 0.4))

keys = dict.keys()
numKeys = len(dict.keys())
tick_labels = ['','','','']

for key in dict.keys():
    axes.semilogx(dict[key]['cpLh'], dict[key]['rank'], 'ko')
    tick_labels[dict[key]['rank']] = key

axes.set_xlabel('Cost per Kilolumen-Hour (USD)')
axes.set_ylabel('')
#axes.set_title('Lumen-Hour Cost')
axes.set_yticks(range(numKeys))
axes.set_xlim((0.05,10))
axes.set_ylim((-0.5, numKeys - 0.5))

#axes.set_yticklabels(keys)
axes.set_yticklabels(tick_labels)
axes.grid(ls='-', color='#dddddd')

fig.savefig('cost_per_lh.pdf')

plt.close()



