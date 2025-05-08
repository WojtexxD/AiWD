import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('footfall_shopping_centers.csv')
x = df['date']
y1 = df['mall_A']
y2 = df['mall_B']
y3 = df['mall_C']

fig, ax = plt.subplots()
ax.scatter(x, y1, color='green', alpha=0.7, s=70, marker='s', label='Mall A')
ax.scatter(x, y2, color='orange', alpha=0.7, s=70, marker='D', label='Mall B')
ax.scatter(x, y3, color='brown', alpha=0.7, s=70, marker='^', label='Mall C')
ax.grid(True, alpha=0.3)
ax.set_xlabel('Data')
ax.set_ylabel('Sprzedaż')
ax.set_title('Porównanie sprzedaży sklepów')
ax.legend(title='Sieć sklepów')
fig.autofmt_xdate()
plt.tight_layout()
plt.savefig('zad4.eps', format='eps')
plt.show()
