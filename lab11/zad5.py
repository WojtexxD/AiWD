import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df1 = pd.DataFrame({
                    'Punkty (%)': [65, 78, 90, 55, 82, 74, 88, 91, 67, 59]
                    })

plt.hist(df1['Punkty (%)'],3,edgecolor='black',alpha=0.7)
plt.title('Punkty w procentach')
plt.xlabel('Ilość osób')
plt.ylabel('Ilość punktów (%)')
plt.grid(True,alpha=0.1)
plt.xticks(np.arange(55,92,12))

plt.show()