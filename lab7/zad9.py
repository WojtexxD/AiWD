import pandas as pd
import numpy as np

pomiary = pd.DataFrame({
'Pomiar': ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9',
'P10'],
'Wartość': [120, 125, 118, 122, 130, 200, 119, 124, 50, 127]
})

Q1 = pomiary['Wartość'].quantile(0.25)
Q3 = pomiary['Wartość'].quantile(0.75)
IQR = Q3-Q1

dolna_granica = Q1-1.5*IQR
gorna_granica = Q3+1.5*IQR

odstajace = pomiary[(pomiary['Wartość']<dolna_granica)|(pomiary['Wartość']>gorna_granica)]
print(odstajace)