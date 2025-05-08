import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [2,3,4,5,6,7,8]
y = [50,55,65,70,75,80,85]
plt.scatter(x,y,color='black', marker='o', s=80)
plt.scatter(x,y, marker='o', s=60)
plt.xlabel('Godziny nauki')
plt.ylabel('Wynik egzaminu (%)')
plt.title('Zależność między godzinami nauki a wynikiem egzaminu')
plt.tight_layout()
plt.show()