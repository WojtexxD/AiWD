import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

punkty = pd.read_csv('ecom_campaigns.csv')
x1 = punkty['visits_campaign_A']
y1 = punkty['orders_campaign_A']
x2 = punkty['visits_campaign_B']
y2 = punkty['orders_campaign_B']
x3 = punkty['visits_campaign_C']
y3 = punkty['orders_campaign_C']
plt.figure()
plt.scatter(x1,y1,color='green',marker='s',s=70,alpha=0.7,label='campain A')
plt.scatter(x2,y2,color='orange',marker='D',s=70,alpha=0.7,label='campain B')
plt.scatter(x3,y3,color='brown',marker='^',s=70,alpha=0.7,label='campain C')
plt.grid(True, alpha=0.3)
plt.xlabel('ilość wizyt')
plt.ylabel('ilość zamówień')
plt.title('wyniki kampanii reklamowej')
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('zad3.webp', format='webp')
plt.show()