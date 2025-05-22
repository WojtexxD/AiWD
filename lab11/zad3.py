import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df1 = pd.DataFrame({
                    'Sklep': ['Sklep A'] * 5 + ['Sklep B'] * 5 + ['Sklep C'] * 5,
                    'Cena (zł/kg)': [3.5, 3.6, 3.7, 3.4, 3.8,
                    3.9, 4.0, 3.8, 4.1, 3.7,
                    4.2, 4.1, 4.3, 4.0, 4.2]
                    })
grupy = df1['Sklep'].unique()
lista_sklepow = [df1.loc[df1['Sklep'] == s, 'Cena (zł/kg)']
                for s in grupy]

fig, ax = plt.subplots()

ax.boxplot(lista_sklepow,tick_labels=grupy,patch_artist=True,#notch=True,
           boxprops=dict(facecolor='palegreen', edgecolor='darkgreen'),
           medianprops=dict(color='darkred'),
           whiskerprops=dict(color='darkgreen'),
           capprops=dict(color='darkgreen'),
           flierprops=dict(marker='o', markerfacecolor='gray', markersize=5, linestyle='none'))

ax.set_title('Rozkład cen w poszczególnych sklepach')
ax.set_xlabel('Sklepy')
ax.set_ylabel('Cena (zł/kg)')
ax.grid(axis='y',linestyle='--',alpha=0.7)
fig.tight_layout()
plt.show()