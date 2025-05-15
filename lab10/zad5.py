import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('restauracje14.csv', sep=';',thousands=' ')
df = pd.melt(df, id_vars='Województwo', var_name='Rok',value_name='Wartość')
df['Rok'] = df['Rok'].astype(int)
w1 = df[df['Województwo']=='KUJAWSKO-POMORSKIE'].reset_index(drop=True)
w2 = df[df['Województwo']=='PODLASKIE']
w3 = df[df['Województwo']=='MAŁOPOLSKIE']
lata = w1['Rok']
width = 0.3
plt.figure()
plt.bar(lata-width,w1['Wartość'],width,color='skyblue',label='Kujawsko-Pomorskie')
plt.bar(lata,w2['Wartość'],width,color='peachpuff',label='Podlaskie')
plt.bar(lata+width,w3['Wartość'],width,color='palegreen',label='Małopolskie')
plt.grid(True,linestyle='--',alpha=0.5)
plt.legend(loc='right')
plt.xlabel('Rok')
plt.ylabel('Liczba restauracji')
plt.title('Liczba restauracji w latach 2016-2021 w wybranych województwach')
plt.tight_layout()
plt.xticks(lata)
plt.yticks(np.arange(0,701,100))
plt.show()