import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sporty=['Piłka nożna','Koszykówka','Tenis','Siatkówka','Hokej']
dzieci=np.array([10,25,35,23,55])
mlodziez=np.array([20,25,15,30,20])
kobiety=np.array([25,20,30,20,10])
ind=np.arange(len(sporty))
width=0.5
plt.figure()
plt.bar(ind,dzieci,width=width,label='Dzieci',color='sandybrown')
plt.bar(ind,mlodziez,width=width,label='Młodzież',bottom=dzieci,color='mediumturquoise')
plt.bar(ind,kobiety,width=width,label='Kobiety',bottom=dzieci+mlodziez,color='lightskyblue')
plt.ylabel('Liczba uczestników (w tys.)')
plt.xlabel('Dyscypliny sportu')
plt.title('Uczestnictwo w różnych dyscyplinach sportu')
plt.xticks(ind,sporty)
plt.legend(loc='upper left')
plt.grid(True,linestyle='--',alpha=0.5,axis='y')
plt.tight_layout()
plt.savefig('zad3.webp',format='webp')
plt.show()