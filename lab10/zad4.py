import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel('handel13.xlsx')
df1 = df[df['Wyszczególnienie']=='stacje paliw']

color = ['lightblue','peachpuff','green','pink','mediumpurple','red','purple','yellow','orange','blue']
width = 0.45
plt.bar(df1['Rok'],df1['Wartosc'], color=color, width=width)
plt.title('Sprzedaż produktu na stacjach paliw w latach 2011-2020')
plt.xlabel('Rok')
plt.xticks(df1['Rok'])
plt.ylabel('Sprzedaż [ob.]')
plt.grid(True, linestyle='--',alpha=0.5, axis='y')
plt.tight_layout()
plt.show()