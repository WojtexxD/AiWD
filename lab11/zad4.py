import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df2 = pd.DataFrame({
                    'Kategoria': ['Elektronika'] * 5 + ['Meble'] * 5 + ['Książki'] * 5,
                    'Czas dostawy (dni)': [2, 3, 1, 2, 2,
                    5, 6, 4, 5, 5,
                    1, 2, 1, 2, 1]
                    })

grupy = df2['Kategoria'].unique()
lista_dostaw = [df2.loc[df2['Kategoria'] == s, 'Czas dostawy (dni)']
                for s in grupy]

fig, ax = plt.subplots()

ax.boxplot(lista_dostaw,tick_labels=grupy,patch_artist=True,#notch=True,
           boxprops=dict(facecolor='palegreen', edgecolor='darkgreen'),
           medianprops=dict(color='darkred'),
           whiskerprops=dict(color='darkgreen'),
           capprops=dict(color='darkgreen'),
           flierprops=dict(marker='o', markerfacecolor='gray', markersize=5, linestyle='none'))

ax.set_title('Rozkład dostaw w dniach')
ax.set_xlabel('Kategorie')
ax.set_ylabel('dni')
ax.grid(axis='y',linestyle='--',alpha=0.7)
fig.tight_layout()
plt.show()