import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x1 = [1000,1500,2000,2500,3000]
y1 = [50,70,90,120,150]
x2 = [900,1200,1600,2000,2400]
y2 = [40,60,80,100,130]
plt.figure()
plt.scatter(x1,y1,color='blue',marker='o',s=50, label='A')
plt.scatter(x2,y2,color='red',marker='^',s=50, label='B')
plt.grid(True, alpha=0.3    )
plt.xlabel('Budżet reklamowy [PLN]')
plt.ylabel('Sprzedaż [sztuki]')
plt.title('Sprzedaż vs budżet reklamowy')
plt.legend(loc='upper left')
plt.savefig('zad1.jpg', format='jpg')
plt.show()
