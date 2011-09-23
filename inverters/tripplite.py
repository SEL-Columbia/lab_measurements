import matplotlib.pyplot as plt   # version 1.0.1
import numpy as np                # version 1.5.1

v_in = 12.0
v_out = 230.0
i_in_noload = 0.55
p_in_noload = v_in * i_in_noload
print 'no load power is ', p_in_noload, ' watts'
r = [10000, 5000, 2500]
i_in = [0.95, 1.36, 2.22]
p_in = [v_in * i_in[x] for x in range(len(i_in))]
print 'power in = ', p_in, ' watts'
p_out = np.square(v_out) / r
print 'power out = ', p_out, 'watts'
#insert no-load-power:
eff = p_out / p_in
eff = np.insert(eff,0,0)
p_out = np.insert(p_out,0,0)
#print p_out
print 'efficiency = ', eff
plt.plot(p_out, eff, label='efficiency')
plt.ylabel('efficiency')
plt.xlabel('load (watts)')
plt.title('tripplite inverter efficiency')
plt.legend(loc=0)
plt.grid(True)
plt.show()
