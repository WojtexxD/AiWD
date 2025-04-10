import pandas as pd

produkty = pd.DataFrame({
'ID': range(1, 11),
'Kategoria': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'],
'Cena': [120, 85, 110, 150, 95, 130, 200, 90, 125, 175],
'Ilość_sprzedana': [450, 320, 380, 290, 410, 360, 240, 350, 400,
270],
'Ocena_klientów': [4.5, 3.8, 4.2, 4.7, 3.9, 4.3, 4.8, 4.0, 4.4, 4.6]
})

print('Statystyki opisowe: ', produkty.describe())
for kol in ['Cena', 'Ilość_sprzedana', 'Ocena_klientów']:
    print(f'\n{kol}')
    print('Skośność: ', produkty[kol].skew())
    print('Kurtoza: ', produkty[kol].kurtosis())