import matplotlib.pyplot as plt   # version 1.0.1
import numpy as np                # version 1.5.1

import datetime as dt
today = dt.datetime.now()

R = [4980, 9950, 19900, 14200, 2490, 994, 500]
R = np.flipud(np.sort(R))
Vrms = 125.0
pred_power = [np.square(Vrms)/R[x] for x in range(len(R))]
print pred_power
belkin = [3.2, 1.6, 0.8, 1.1, 6.3, 15.6, 31.0]
belkin = np.sort(belkin)
sc20_1 = [2.3, 0.8, 0, 0, 5.5, 14.8, 30.4]
sc20_2 = [2.7, 1.1, 0, 0, 5.8, 15.2, 30.8]
sc20_1 = np.sort(sc20_1)
sc20_2 = np.sort(sc20_2)
mains_measured = [31.0, 29.4, 28.6, 29, 34.1, 43.6, 59.5]
mains_measured = np.sort(mains_measured)
baseline = np.ones(len(R)) * 27.9
sc20_mains = mains_measured - baseline

fig = plt.figure()
ax = fig.add_axes((.1,.3,.8,.6))
ax.loglog(pred_power, sc20_mains, 'x-', color='r', label='Mains')
ax.loglog(pred_power, pred_power, '-', color='k', label='ideal')
ax.loglog(pred_power, [pred_power[x]*.9 for x in range(len(pred_power))], '-', color='0.75', label='-10%')
ax.loglog(pred_power, [pred_power[x]*1.1 for x in range(len(pred_power))], '-', color='0.75', label='+10%')
ax.loglog(pred_power, sc20_1, '^-', color='b', label='sc20_1')
ax.loglog(pred_power, sc20_2, '^-', color='g', label='sc20_2')
ax.legend(loc=0)
ax.set_ylim((0,35))
ax.set_xlim((0,35))
ax.set_xlabel('predicted power (watts)')
ax.set_ylabel('measured power (watts)')
#ax.set_xticklabels(np.exp(
fileNameString = 'log-log plot of power measurement error on sc20 circuits and mains'
ax.set_title(fileNameString)
annotation = []
annotation.append('plot generated ' + today.__str__() )
annotation.append('function = ' + 'sc20powerConsumption')
annotation.append('data points at predicted power of: ' + str(np.round(pred_power,2)))
annotation = '\n'.join(annotation)
#plt.show()
fig.text(0.01,0.01, annotation) #, fontproperties=textFont)
fig.savefig('plots/'+fileNameString+'.pdf')
plt.close(fig)

sc20_mains_error = np.round(np.abs(sc20_mains - pred_power)*100/pred_power,2)
sc20_1_error = np.round(np.abs(sc20_1 - pred_power)*100/pred_power,2)
sc20_2_error = np.round(np.abs(sc20_2 - pred_power)*100/pred_power,2)
fig2 = plt.figure()
ax2 = fig2.add_axes((.1,.3,.8,.6))
ax2.plot(pred_power, sc20_mains_error, 'x-', color='r', label='mains')
ax2.plot(pred_power, sc20_1_error, '^-', color='b', label='sc20_1')
ax2.plot(pred_power, sc20_2_error, '^-', color='g', label='sc20_2')
ax2.legend(loc=0)
#ax2.set_ylim((0,35))
ax2.set_xlim((0,35))
ax2.set_xlabel('predicted power (watts)')
ax2.set_ylabel('precentage error (%)')
#ax.set_xticklabels(np.exp(
fileNameString2 = 'plot of power measurement error on sc20 circuits and mains'
ax2.set_title(fileNameString2)
annotation2 = []
annotation2.append('plot generated ' + today.__str__() )
annotation2.append('function = ' + 'sc20powerConsumption')
annotation2.append('data points at predicted power of: ' + str(np.round(pred_power,2)))
annotation2 = '\n'.join(annotation2)
#plt.show()
fig2.text(0.01,0.01, annotation2) #, fontproperties=textFont)
fig2.savefig('plots/'+fileNameString2+'.pdf')
