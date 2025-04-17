import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel('cena_paliwa11.xlsx')

df1 = df[df['Rodzaj paliwa'] == 'Benzyna 95']

x = df1[df1['Rok'] == 2015]['Miesiące']
y1 = df1[df1['Rok'] == 2015]['Wartosc']
y2 = df1[df1['Rok'] == 2016]['Wartosc']
plt.figure(figsize=(8, 8))
plt.plot(x, y1, linestyle='--', color='olive', linewidth=2, label='2015')
plt.plot(x, y2, linestyle='-', color='lime', linewidth=3, label='2016')
plt.grid(True)
plt.legend(loc='lower left')
plt.title('Cena paliwa w latach')
plt.xlabel('Miesiące')
plt.ylabel('Cena (zł)')
plt.savefig('ceny-paliwa.png', format='png')
plt.show()
