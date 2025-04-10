import pandas as pd

pracownicy = pd.DataFrame({
'Imię': ['Anna', 'Bartek', 'Celina', 'Dawid', 'Ewa', 'Filip',
'Gosia', 'Hubert', 'Iza', 'Jan'],
'Dział': ['IT', 'Marketing', 'HR', 'IT', 'Marketing', 'HR', 'IT',
'Marketing', 'HR', 'IT'],
'Wynagrodzenie': [7500, 6800, 5900, 8200, 7000, 6100, 7800, 6500,
6000, 8500],
'Staż_lat': [3, 5, 2, 7, 4, 1, 6, 3, 2, 8]
})

print(pracownicy.groupby('Dział')['Wynagrodzenie'].agg(['count', 'mean', 'median', 'std', 'min', 'max']))
print(pracownicy.groupby('Dział')['Wynagrodzenie'].describe().T)