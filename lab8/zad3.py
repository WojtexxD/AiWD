import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(-3, 0.9, 100)
y1 = np.exp(4*x)
y2 = 2*np.cos(3*x)
y3 = x**2 + 4

plt.plot(x,y1, linestyle=':',color='r', label=r'$y=e^{4x}$')
plt.plot(x,y2, linestyle='-', color='b', label=r'$y=2cos(3x)$')
plt.plot(x,y3, linestyle='--', color='g', label=r'$y=x^{2}+4$')
plt.grid(True)
plt.legend(loc='upper left')
plt.title('Wykres trzech funkcji')
plt.xticks(np.arange(-3,1.1))
plt.show()