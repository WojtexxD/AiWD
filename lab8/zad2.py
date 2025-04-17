import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('ceny23.csv', sep=';', decimal=',')

df1 = df[df['Rodzaje towarów i usług'] == 'pomarańcze - za 1kg']

x = df1['Miesiące']
y = df1['Wartosc']
plt.figure(figsize=(8,8))
plt.plot(x,y, linestyle='--', color='orange', linewidth='4', label='2017')
plt.grid(True)
plt.legend(loc='upper right')
plt.savefig('ceny_pomaranczy.webp', format='webp')
plt.show()