import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(2,4.9,100)
y1 = x + 4
y2 = np.sin(2*x)
fig, ax = plt.subplots()
ax.plot(x,y1, linestyle=':', color='red', label=r'$x+4$')
ax.set_ylabel('oś pionowa po lewej stronie', color='green')
ax.set_xlabel('oś pozioma')
ax.set_ylim(-12,12)
ax.set_yticks(np.arange(-10,10.1,5))
ax.set_title('Wykresy - kilka')
ax.legend(loc='upper left')

ax2 = ax.twinx()
ax2.plot(x,y2, linestyle=':', color='saddlebrown', label=r'$sin(2x)$')
ax2.set_ylabel('oś pionowa po prawej stronie')
ax2.set_ylim(-2,2)
ax2.legend(loc='lower center')

fig.tight_layout()
plt.show()