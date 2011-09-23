import matplotlib.pyplot as plt   # version 1.0.1
import numpy as np                # version 1.5.1

voltage = np.flipud(np.arange(1.0,3.3,0.1))
voltage = np.delete(voltage, [2,16])  # take out 3. and 1.6 that didnt have direct data
current = [129,109, 90, 73, 60, 50.5, 45.75, 45.5, 46.1, 45.8, 44.8, 42.8, 40, 37.4, 35.1, 33.25, 32.5, 33.6, 32.1, 23.5, 10.4]
lux = [2700,2500,2290,2000,1705,1444,1272,1218,1186,1134,1065,982,891,800,715,642,571,459,253,95,12]
distance = np.arange(0,24,1)
lux_at_d = [2570,2020,1270,563,282,180,120,86,67,55,48,41,37,33,30,28,24,18,11,8,6,4,2,0]

fig=plt.figure()
fig,axs = plt.subplots(3,1)
axs[0].plot(voltage, current)
axs[0].invert_xaxis()
axs[0].set_title('I-V curve')
axs[1].plot(voltage, lux)
axs[1].invert_xaxis()
axs[1].set_title('lux vs. voltage')
axs[2].plot(distance, lux_at_d)
axs[2].set_title('lux vs. horizontal distance, at 25cm height')
fig.savefig('plots/flashlight.pdf')

