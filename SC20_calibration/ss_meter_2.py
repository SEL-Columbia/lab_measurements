import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sint

d = np.loadtxt('ss_meter_2.csv',skiprows=2,usecols=[0,1,2],delimiter=',')

# calibration factors
voltage_divider = 100
r_shunt = 1
mA_per_A = 1000

# voltage on channel 1
# current on channel 2
t = d[:, 0]
v = d[:, 1] * voltage_divider
i = d[:, 2] / r_shunt

# subtract mean from v and i
v = v - np.mean(v)
i = i - np.mean(i)

# instantaneous power
p = v * i


# find zero time
int_start = np.argmin(abs(t - 0.0))
# find time after one period
period = 1 / 60.0
int_end = np.argmin(abs(t - period))

# rms current and voltage
v_rms = np.sqrt(np.mean(v[int_start:int_end] ** 2))
i_rms = np.sqrt(np.mean(i[int_start:int_end] ** 2))

print 'rms voltage =', v_rms
print 'rms current =', i_rms

# integrate to get real power
e = sint.trapz(p[int_start:int_end], t[int_start:int_end])
real_power = e / period

apparent_power = v_rms * i_rms


print 'real power =', real_power
print 'apparent power =', apparent_power

print 'power factor =', real_power / apparent_power

plt.plot(t, i * mA_per_A, label='current (mA)')
plt.plot(t, v, label='voltage (V)')
plt.plot(t, p, label='power (W)')
plt.title('meters on 120VAC/60Hz voltage, current, and power')
plt.legend()
plt.show()

