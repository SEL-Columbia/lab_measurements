import matplotlib.pyplot as plt   # version 1.0.1
import numpy as np                # version 1.5.1

circuits = [201,202,203,204]
res = [5000, 2500, 1000, 500]
res_watts = [(np.square(120.0)/res[x]) for x in range(len(res))]
loads = [0] + res_watts

main_read = np.zeros((len(circuits), len(res_watts)))
main_noload = [38.05,37.8,37.95,38.05]
main_read[0] = [41.4,44.65,54.45,70.6]
main_read[1] = [41.0,44.3,54.0,70.4]
main_read[2] = [41.35,44.6,54.25,70.55]
main_read[3] = [41.35,44.65,54.25,70.6]
for i in range(len(main_read)):
    main_read[i] = main_read[i] - main_noload
print main_read
cct_read = np.zeros((len(circuits), len(res_watts)))
cct_read[0] = [2.2,5.55,15.25,32]
cct_read[1] = [2.85,6.1,15.75,31.9]
cct_read[2] = [2.85,6.2,15.85,32.25]
cct_read[3] = [2.75,6.1,15.85,32.1]
#cctreads = np.zeros((len(circuits), len(loads)))
for i in range(len(loads)):
    cctreads = np.insert(cct_read, 0, 0, 1)
print cctreads
fig=plt.figure()
ax = fig.add_axes((.1,.3,.8,.6))
#fig,axs = plt.subplots(2,1)
for i in range(len(main_read)):
    ax.plot(res_watts, main_read[i]-cct_read[i], 'x-', label=str(circuits[i]))
ax.legend(loc=0)
ax.set_xlabel("load (watts)")
ax.set_ylabel("difference (watts)")
ax.set_title("difference between circuit and main meter readings")
fig.savefig('plots/sc20powerReadingDiffs.pdf')

fig1=plt.figure()
ax1 = fig1.add_axes((.1,.3,.8,.6))
#fig,axs = plt.subplots(2,1)
for i in range(len(cctreads)):
    ax1.plot(loads, cctreads[i]-loads, 'x-', label=str(circuits[i]))
ax1.legend(loc=0)
ax1.set_xlabel("loads (watts)")
ax1.set_ylabel("difference (watts)")
ax1.set_title("difference between sc20 measured and real power")
fig1.savefig('plots/sc20readingdiffs.pdf')

fig2=plt.figure()
ax2 = fig2.add_axes((.1,.3,.8,.6))
#fig,axs = plt.subplots(2,1)

#perc = np.array((len(cctreads),len(loads)))
#perc = np.zeros((len(circuits),len(loads)))
perc = [[]*len(loads)]*len(cctreads)
#print perc
for i in range(len(circuits)):
    perc[i] = (cct_read[i]-res_watts)/res_watts
#for i in range(len(circuits)):
    perc[i] = np.insert(perc[i],0,0)
print perc
'''
perc = [[]*len(loads)]*len(cctreads)
for i in range(len(cctreads)):
    perc[i] = [0] + ((cct_read[i]-res_watts)/res_watts)
'''
print perc
for i in range(len(cctreads)):
    ax2.plot(loads, perc[i], 'x-', label=str(circuits[i]))
ax2.legend(loc=0)
ax2.set_xlabel("loads (watts)")
ax2.set_ylabel("difference (% watts)")
ax2.set_title("percent difference between sc20 measured and real power")
fig2.savefig('plots/sc20percentDiffs.pdf')
