import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df3 = pd.DataFrame({
                    'Typ rozmowy': ['Przychodzące'] * 8 + ['Wychodzące'] * 7,
                    'Czas (minuty)': [5, 3, 7, 2, 10, 4, 6, 8, 9, 12, 7, 5, 4, 11, 3]
                    })

plt.hist(df3['Czas (minuty)'],4,edgecolor='black',alpha=0.7) # w bins [2,5,8,10,12] sami ustawiamy przedzialy
plt.title('Analiza długości rozmów telefonicznych')
plt.xlabel('Czas rozmowy w minutach')
plt.ylabel('Ilość połączeń')
plt.grid(True,alpha=0.1)
plt.xticks(np.arange(2,13))

plt.show()