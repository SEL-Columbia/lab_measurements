from __future__ import division
import matplotlib.pyplot as plt

def addEntry(key, cost, energy):
    dict[key] = {}
    dict[key]['cost'] = cost
    dict[key]['energy'] = energy
    dict[key]['cpkWh'] = dict[key]['cost'] / dict[key]['energy']

dict = {}

addEntry('Cell Phone Charge',  cost = 0.25, energy = 0.005)
#addEntry('Kerosene',    cost = 1.20, energy = 45/3.6)
addEntry('D Cell',      cost = 0.30, energy = 0.0022)
addEntry('Car Battery Charge', cost = 1.0,  energy = 0.12)
#addEntry('SharedSolar', cost = 1.0,  energy = 0.2)
addEntry('Grid Mali',   cost = 16,   energy = 16/0.2)

fig = plt.figure()
axes = fig.add_subplot(111)

for key in dict.keys():
    axes.loglog(dict[key]['cost'], dict[key]['cpkWh'], 'ko')
    axes.text(dict[key]['cost'], dict[key]['cpkWh'], key)

from matplotlib.patches import Rectangle

rect = Rectangle((1, 1), 4, 5, facecolor="#dddddd")
axes.add_artist(rect)
#rect.set_clip_box(axes.bbox)
axes.text(1.3,2,'Shared Solar')

plt.xlim((0.1,50))
plt.ylim((0.01,500))

plt.title('Unit Cost of Energy and Purchase Price')
plt.xlabel('Purchase Cost (USD)')
plt.ylabel('Cost Per kWh')

plt.grid()
plt.savefig('costVsEnergy.pdf')
plt.show()

plt.close()