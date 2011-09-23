import matplotlib.pyplot as plt   # version 1.0.1
import numpy as np                # version 1.5.1

#from __future__ import division

def addEntry(key, chem, cost, energy):
    dict[key] = {}
    dict[key]['chem'] = chem
    dict[key]['cost'] = cost
    dict[key]['energy'] = energy
    dict[key]['cpkWh'] = dict[key]['cost'] / dict[key]['energy']

dict = {}

addEntry(1, chem='SLA',  cost = 165, energy = 0.6)
addEntry(2, chem='SLA',  cost = 64.6, energy = 0.24)
addEntry(3, chem='SLA',  cost = 34.85, energy = 0.108)
addEntry(4, chem='SLA',  cost = 16, energy = 0.0144)
addEntry(5, chem='SLA',  cost = 45.55, energy = 0.144)
addEntry(6, chem='SLA',  cost = 55.65, energy = 0.216)
addEntry(7, chem='SLA',  cost = 225, energy = 1.2)
addEntry(8, chem='SLA',  cost = 170, energy = .66)
addEntry(9, chem='SLA',  cost = 198, energy = .9)
#addEntry('Kerc=colormap[m]osene',    cost = 1.20, energy = 45/3.6)
addEntry(10, chem='Lithium', cost = 13, energy = 0.0039)
addEntry(11, chem='Lithium', cost = 7, energy = 0.00962)
addEntry(12, chem='Lithium', cost = 50, energy = 0.066)
addEntry(13, chem='Lithium', cost = 11250, energy = 25)
addEntry(14, chem='NiMH', cost = 6.45,  energy = 0.006)
addEntry(15, chem='NiMH', cost = 9.6,  energy = 0.012)
addEntry(16, chem='NiMH', cost = 7.3,  energy = 0.009)
addEntry(17, chem='NiMH', cost = 8,  energy = 0.0108)
#addEntry('SharedSolar', cost = 1.0,  energy = 0.2)
#addEntry('Advanced LA',   cost = 16,   energy = 16/0.2)

fig = plt.figure()
axes = fig.add_subplot(111)

colormap = ['b','g','r','c','m','y','k','brown', 'deeppink','darkslateblue','dimgray','indigo','lightseagreen']
mkr = ['.',',','o','v','^','<','>','1','2','3','4','s','p','*','h','H','+','x','D','d','|','_']
for key in dict.keys():
    axes.loglog(dict[key]['energy'], dict[key]['cpkWh'], c=colormap[len(dict[key]['chem'])-3], marker=mkr[len(dict[key]['chem'])-3], label=str(dict[key]['chem']))
    #axes.text(dict[key]['cost'], dict[key]['cpkWh'], key)
#axes.legend(('SLA', 'Lithium', 'NiMH'))
axes.legend(loc=0)

'''
from matplotlib.patches import Rectangle

rect = Rectangle((1, 1), 4, 5, facecolor="#dddddd")
axes.add_artist(rect)
#rect.set_clip_box(axes.bbox)
axes.text(1.3,2,'Shared Solar')
'''

plt.xlim((-10,50))
plt.ylim((10,5000))

plt.title('Unit Cost of Energy and Purchase Price')
plt.xlabel('Battery Capacity (kWh)')
plt.ylabel('Cost Per kWh')

plt.grid()
plt.savefig('costVsCapacity.pdf')
plt.show()

plt.close()
