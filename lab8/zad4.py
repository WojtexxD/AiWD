import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(-3,0.9, 100)
y1 = -x**2+4
y2 = np.exp(x)+4
y3 = 2*np.cos(3*x)
plt.plot(x,y1, linestyle='--', color='orange', label=r'$y=-x^{2}+4$')
plt.plot(x,y2, linestyle=':', color='g', label=r'$y=e^{x}+4$')
plt.plot(x,y3, linestyle='-', color='violet', label=r'$y=2cos(3x)$')
plt.grid(True)
plt.xticks(np.arange(-3,1.1))
plt.legend(loc='lower right')
plt.title('Wykres trzech funkcji')
plt.show()