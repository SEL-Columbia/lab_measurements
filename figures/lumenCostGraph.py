from __future__ import division
import matplotlib.pyplot as plt

def addEntry(key, cost, cpLh):
    dict[key] = {}
    dict[key]['cost'] = cost
    dict[key]['cpLh'] = cpLh

dict = {}

addEntry('Kerosene',             cost = 1.20, cpLh = 1)
addEntry('D Cell',               cost = 0.30, cpLh = 4.3)
addEntry('Car Battery With CFL', cost = 1.0,  cpLh = 0.12)
#addEntry('SharedSolar With CFL', cost = 1.0,  cpLh = 0.10)
#addEntry('Grid Mali With CFL',   cost = 16,   cpLh = 16/0.2)

fig = plt.figure()
axes = fig.add_subplot(111)

for key in dict.keys():
    axes.loglog(dict[key]['cost'], dict[key]['cpLh'], 'ko')
    axes.text(dict[key]['cost'], dict[key]['cpLh'], key)

from matplotlib.patches import Rectangle

rect = Rectangle((1, .017), 5, .07, facecolor="#dddddd")
axes.add_artist(rect)
rect.set_clip_box(axes.bbox)

axes.text(1.1,0.03, 'Shared Solar With CFL')

plt.xlim((0.1,10))
plt.ylim((0.01,10))

plt.title('Lumen-Hour Cost vs. Purchase Price')
plt.xlabel('Purchase Cost (USD)')
plt.ylabel('Cost Per Lumen-Hour')

plt.grid()
plt.savefig('costVsLumens.pdf')
plt.show()

plt.close()