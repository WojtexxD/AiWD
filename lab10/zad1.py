import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x1 = [40,20,15,15,10]
x2 = [25,20,18,15,12,10]
c1 = ['lightcoral','skyblue','mediumturquoise','sandybrown','plum']
c2 = ['lightskyblue','palegreen','moccasin','pink','mediumpurple','lightgray']
labels1 = ['Piłka nożna','Koszykówka','Tenis','Siatkówka','Hokej']
labels2 = ['Lekkoatletyka','Pływanie','Boks','Gimnastyka','Kolarstwo','Golf']
explode1 = (0.1, 0, 0, 0, 0)
explode2 = (0.1,0,0,0,0,0)
plt.axis('equal')
fig, ax = plt.subplots(2,1)
ax[0].pie(x1, explode=explode1, labels=labels1, colors=c1, autopct='%1.1f%%', startangle=90)
ax[1].pie(x2, explode=explode2, labels=labels2, colors=c2, autopct='%1.1f%%', startangle=90)
fig.suptitle('Popularność dyscyplin sportowych')
fig.tight_layout()
plt.savefig('zad1.png', format='png')
plt.show()