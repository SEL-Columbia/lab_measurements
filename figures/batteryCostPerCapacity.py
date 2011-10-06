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

#d = np.loadtxt('csv/battery_prices.csv',skiprows=1,usecols=[0,3,4,6],delimiter=',', dtype=[('chem',str),('cap',float),('model',str),('price',float)] )
#d = np.loadtxt('csv/battery_prices.csv',skiprows=1,usecols=[0,3,4,6],delimiter=',', dtype=None )
d = np.loadtxt('csv/battery_prices.csv',skiprows=1,usecols=[0,3,5,7],delimiter=',', dtype=str )
#d = np.loadtxt('csv/battery_prices.csv',skiprows=1,usecols=[0,3,4,6],delimiter=',', dtype={'names': ('chem', 'cap', 'model','price'),'formats': ('S1', 'f4','S1', 'f4')} )
#d = np.genfromtxt('csv/battery_prices.csv',skiprows=1,usecols=[0,3,4,6],delimiter=',', filling_values=0 ,dtype=[('chem','S5'),('cap','f8'),('model','S5'),('price','f8')] )
#d = np.genfromtxt('csv/battery_prices.csv',skip_header=1,skip_footer=1,usecols=[0,3,4,6],delimiter=',', filling_values=0 ,dtype=None, names=['chem','cap','model','price'] )
#d = np.genfromtxt('csv/battery_prices.csv',skip_header=1,skip_footer=1,usecols=[0,3,4,6],delimiter=",", filling_values=0 ,dtype="S5,f8,S5,f8", names=['chem','cap','model','price'] )

chem = [d[x,0].replace('"','') for x in range(len(d))]
cap = [float(d[x,1]) for x in range(len(d))]
cap_kwh = [cap[x]/1000 for x in range(len(cap))]
#cap_kwh = d['cap']/1000
model = [d[x,2].strip('"') for x in range(len(d))]
price = [float(d[x,3]) for x in range(len(d))]
#cpkwh = price / cap_kwh
#cpkwh = d['price'] / cap_kwh
cpkwh = [price[x]/cap_kwh[x] for x in range(len(price))]

'''
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
'''

fig = plt.figure()
axes = fig.add_subplot(111)

colormap = ['b','g','r','c','m','y','k','brown', 'deeppink','darkslateblue','dimgray','indigo','lightseagreen']
mkr = ['.',',','o','v','^','<','>','1','2','3','4','s','p','*','h','H','+','x','D','d','|','_']

'''
for key in dict.keys():
    axes.loglog(dict[key]['energy'], dict[key]['cpkWh'], c=colormap[len(dict[key]['chem'])-3], marker=mkr[len(dict[key]['chem'])-3], label=str(dict[key]['chem']))
    #axes.text(dict[key]['cost'], dict[key]['cpkWh'], key)
#axes.legend(('SLA', 'Lithium', 'NiMH'))
axes.legend(loc=0)
'''

for i in range(len(d)):
    if chem[i]=='SLA':
        color = 'k'
        mkr = 's'
    elif chem[i] == 'Lithium':
        color = 'b'
        mkr = 'o'
    elif chem[i] == 'LiFe':
        color = 'b'
        mkr = '*'
    elif chem[i] == 'NiMH':
        color = 'orange'
        mkr = '^'
    else:
        color = 'brown'
        mkr = '+'
    axes.loglog(cap_kwh[i], cpkwh[i], c=color, marker=mkr, ls='None', label=model[i])
    #axes.loglog(cap_kwh, cpkwh, c=color, marker=mkr, label=d['model'][i])
    axes.text(cap_kwh[i],cpkwh[i],'  '+model[i],color=color, fontsize=6, ha='left', va='center')
#axes.legend(('SLA','Lithium','NiMH'))
legendline1='SLA'
legendline2='Lithium'
legendline3='LiFe'
legendline4='NiMH'
axes.plot(0.89, 0.15, 's', color='k', transform=axes.transAxes)
axes.text(0.9, 0.14, legendline1, color = 'k', fontsize=10, transform=axes.transAxes)
axes.plot(0.89, 0.11, 'o', color = 'b', transform=axes.transAxes)
axes.text(0.9,0.1, legendline2, color = 'b', fontsize=10, transform=axes.transAxes)
axes.plot(0.89, 0.07, '*', color = 'b', transform=axes.transAxes)
axes.text(0.9,0.06, legendline3, color = 'b', fontsize=10, transform=axes.transAxes)
axes.plot(0.89,0.03, '^', color = 'orange', transform=axes.transAxes)
axes.text(0.9,0.02, legendline4, color = 'orange', fontsize=10, transform=axes.transAxes)

'''
from matplotlib.patches import Rectangle

rect = Rectangle((1, 1), 4, 5, facecolor="#dddddd")
axes.add_artist(rect)
#rect.set_clip_box(axes.bbox)
axes.text(1.3,2,'Shared Solar')
'''

plt.xlim((-10,50))
plt.ylim((100,5000))

plt.title('Batteries Unit Cost of Energy and Purchase Price')
plt.xlabel('Battery Capacity (kWh)')
plt.ylabel('Cost Per kWh')

plt.grid(color='grey',linestyle='-')
plt.savefig('plots/costVsCapacity.pdf')
plt.show()

plt.close()
