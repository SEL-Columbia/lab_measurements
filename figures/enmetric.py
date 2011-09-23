import matplotlib.pyplot as plt   # version 1.0.1
import numpy as np                # version 1.5.1

circuits = [1,2,3,4]
res = [10000, 5000, 2500, 1000, 500]
res_watts = [(np.square(120.0)/res[x]) for x in range(len(res))]
loads = [0] + res_watts

belkin_read = np.zeros((len(circuits), len(res_watts)))
# belkin readings without loads as circuits turned 'on' from 0 to 4 ccts
belkin_noload = [0.9, 1.1, 1.3, 1.6, 1.9]
belkin_read[0] = [2.6,4.0,7.0,15.7,30.2]
belkin_read[1] = [2.6,4.0,7.0,15.7,30.6]
belkin_read[2] = [2.6,4.1,7.0,15.9,30.6]
belkin_read[3] = [2.6,4.1,7.0,15.8,30.6]
# take off belkin_noload for 1 circuit 'on'
for i in range(len(belkin_read)):
    belkin_read[i] = [(belkin_read[i][x] - belkin_noload[1]) for x in range(belkin_read.shape[1])]
print belkin_read
cct_read = np.zeros((len(circuits), len(res_watts)))
cct_read[0] = [1.12,2.61,5.69,14.63, 29.44]
cct_read[1] = [1.50,3.0,6.03,15.02, 30.26]
cct_read[2] = [1.48,2.99,6.05,15.18, 30.4]
cct_read[3] = [1.47,2.96,6.01,14.98, 30.2]
cct_read_avg = np.average(cct_read,0)
print cct_read_avg

fig=plt.figure()
ax = fig.add_axes((.1,.3,.8,.6))
#fig,axs = plt.subplots(2,1)
for i in range(len(belkin_read)):
    shade = 0.1 + (0.25*i)
    #print shade
    ax.plot(res_watts, res_watts, '-', c='0.5', lw=3)
    ax.plot(res_watts, belkin_read[i], 'x-', c= ((shade, 0, shade)), label='belkin '+str(circuits[i]))
    ax.plot(res_watts, cct_read[i], 'o-', c=((0,shade,shade)), label='circuit '+str(circuits[i]))
ax.legend(loc=0)
ax.set_xlabel("load (watts)")
ax.set_ylabel("readings (watts)")
ax.set_title("enmetric circuit and belkin meter readings")
fig.savefig('plots/enmetricReadings.pdf')

fig1=plt.figure()
ax1 = fig1.add_axes((.1,.3,.8,.6))
#fig,axs = plt.subplots(2,1)
for i in range(len(belkin_read)):
    shade = 0.1 + (0.25*i)
    #print shade
    ax1.plot(res_watts, [res_watts[x]-res_watts[x] for x in range(len(res_watts))], '-', c='0.5', lw=3)
    ax1.plot(res_watts, belkin_read[i]-res_watts, 'x-', c= ((shade, 0, shade)), label='belkin '+str(circuits[i]))
    ax1.plot(res_watts, cct_read[i]-res_watts, 'o-', c=((0,shade,shade)), label='circuit '+str(circuits[i]))
ax1.legend(loc=0)
ax1.set_xlabel("load (watts)")
ax1.set_ylabel("readings' differences (watts)")
ax1.set_title("enmetric circuit meter readings difference from actual load")
fig1.savefig('plots/enmetricDiff.pdf')

fig1b=plt.figure()
ax1b = fig1b.add_axes((.1,.3,.8,.6))
#fig,axs = plt.subplots(2,1)
for i in range(len(belkin_read)):
    shade = 0.1 + (0.25*i)
    #print shade
    ax1b.plot(res_watts, [((res_watts[x]-res_watts[x])/res_watts[x]) for x in range(len(res_watts))], '-', c='0.5', lw=3)
    ax1b.plot(res_watts, (belkin_read[i]-res_watts)/res_watts, 'x-', c= ((shade, 0, shade)), label='belkin '+str(circuits[i]))
    ax1b.plot(res_watts, (cct_read[i]-res_watts)/res_watts, 'o-', c=((0,shade,shade)), label='circuit '+str(circuits[i]))
ax1b.legend(loc=0)
ax1b.set_xlabel("load (watts)")
ax1b.set_ylabel("readings' percent differences (watts)")
ax1b.set_title("enmetric circuit meter readings percent difference from actual load")
fig1b.savefig('plots/enmetricPercentDiff.pdf')

# all switches on
# 6 tests
belkin_read2 = [6.3, 10.7, 22.5, 12.2, 25.4, 26.9]
belkin_read2 = [(belkin_read2[x] - belkin_noload[4]) for x in range(len(belkin_read2))]
cct_read2 = np.zeros((6, len(circuits)))
cct_read2[0] = [1.28, 3.03, 0, 0]
cct_read2[1] = [0, 3.05, 6.07, 0]
cct_read2[2] = [0, 0, 6.07, 15.02]
cct_read2[3] = [1.26, 3.04, 6.07, 0]
cct_read2[4] = [0, 3.04, 6.09, 15.02]
cct_read2[5] = [1.33, 3.05, 6.11, 15.03]
# get average reading for each load
#cct_read_avg2 = np.average(cct_read2,0)
cct_read_avg2 = np.zeros(cct_read2.shape[1])
# remove zeros from cct_read2
for i in range(len(cct_read_avg2)):
    #print cct_read2[:,i]
    cct_read_avg2[i] = np.average(np.take(cct_read2[:,i],np.nonzero(cct_read2[:,i]>0)))
cct_read_avg2 = np.append(cct_read_avg2,0)
fig2=plt.figure()
ax2 = fig2.add_axes((.1,.3,.8,.6))
#fig,axs = plt.subplots(2,1)
ax2.plot(res_watts, res_watts, '-', c='k', label='ideal')
ax2.plot(res_watts, cct_read_avg, 'x-', label='single circuit')
ax2.plot(res_watts, cct_read_avg2, 'o-', label='cross talk?')
ax2.legend(loc=0)
ax2.set_xlabel("loads (watts)")
ax2.set_ylabel("average power (watts)")
ax2.set_title("enmetric average measured power with and without possible crosstalk")
fig2.savefig('plots/enmetricCrossTalk.pdf')
