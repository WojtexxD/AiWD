import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [40,60,80,100,120]
y1 = [8.5,7.2,6.3,5.8,6.1]
y2 = [9.5,8.6,7.9,7.2,7.5]
y3 = [12,11,10,9.5,9]
plt.scatter(x,y1,color='green',s=50, alpha=0.7,marker='s',label='Samochód osobowy')
plt.scatter(x,y2, color='orange',s=50,alpha=0.7,marker='D',label='SUV')
plt.scatter(x,y3,color='brown',s=50,alpha=0.7,marker='^',label='Ciężarówka')
plt.grid(True,alpha=0.3)
plt.xlabel('Prędkość [km/h]')
plt.ylabel('Zużycie paliwa [l/100km]')
plt.title('Zużycie paliwa vs prędkość dla różnych typów pojazdów')
plt.legend(loc='upper right',title='Typ pojazdu')
plt.savefig('zad2.tiff',format='tiff')
plt.show()