import matplotlib.pyplot as plt   # version 1.0.1
import numpy as np                # version 1.5.1

e = np.loadtxt('csv/inverters.csv',skiprows=1,usecols=[0,1,3,4],delimiter=',', dtype=str )


make = [e[x,0].strip('"') for x in range(len(e))]
brands = set(make)
model = [e[x,1].strip('"') for x in range(len(e))]
cap = [float(e[x,2]) for x in range(len(e))]
cap_kwh = [cap[x]/1000 for x in range(len(cap))]

price = [float(e[x,3]) for x in range(len(e))]

cpkwh = [price[x]/cap_kwh[x] for x in range(len(price))]

fig = plt.figure()
axes = fig.add_subplot(111)

colormap = ['b','g','r','c','m','y','k','brown', 'deeppink','darkslateblue','dimgray','indigo','lightseagreen']
markr = ['.',',','o','v','^','<','>','1','2','3','4','s','p','*','h','H','+','x','D','d','|','_']

for i in range(len(e)):
    #check to see which brand item is, getting index in 'brands':
    b = list(brands).index(make[i])
    # use brand index to set color and marker:
    color = colormap[b]
    mkr = markr[b]
    axes.loglog(cap_kwh[i], cpkwh[i], c=color, marker=mkr, ls='None', label=model[i])
    axes.text(cap_kwh[i],cpkwh[i],'  '+model[i],color=color, fontsize=6, ha='left', va='center')

for b in range(len(brands)):
    axes.plot(0.84,0.03+(.04*b), marker=markr[b], color = colormap[b], transform=axes.transAxes)
    axes.text(0.85,0.02+(.04*b), list(brands)[b], color = colormap[b], fontsize=10, transform=axes.transAxes)
plt.xlim((-100,20))
plt.ylim((50,4000))

plt.title('Inverters Unit Cost of Power and Purchase Price')
plt.xlabel('Inverter Output Power (kW)')
plt.ylabel('Cost Per kW')

plt.grid(color='grey',linestyle='-')
plt.savefig('plots/inverterCostVsCapacity.pdf')
plt.show()

plt.close()
