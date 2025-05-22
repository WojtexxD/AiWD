import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(2,4.9,100)
y1 = np.sin(2*x)
y2 = np.exp(2*x)
fig, ax = plt.subplots()
ax.plot(x,y1,linestyle=':', color='saddlebrown', label=r'$sin(2x)$')
ax.set_title('Wykres - kilka')
ax.set_xlabel('oś pozioma')
ax.set_ylabel('oś pionowa po lewej stronie')
ax.set_ylim(-12,12)
ax.legend(loc='upper left')

ax2 = ax.twinx()
ax2.plot(x,y2,linestyle=':', color='darkturquoise', label=r'$e^{2x}$')
ax2.set_ylabel('oś pionowa po prawej stronie', color='blue')
ax2.set_ylim(-750,19000)
ax2.legend(loc='lower center')

fig.tight_layout()
plt.show()