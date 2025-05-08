import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('footfall_shopping_centers.csv')
df2 = pd.melt(df,id_vars='date',value_vars=['mall_A','mall_B','mall_C'],var_name='Mall',value_name='Sales')
x = df2[df2['Mall']=='mall_A']['date']
y1 = df2[df2['Mall']=='mall_A']['Sales']
y2 = df2[df2['Mall']=='mall_B']['Sales']
y3 = df2[df2['Mall']=='mall_C']['Sales']
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
plt.savefig('zad5.png', format='png')
plt.show()