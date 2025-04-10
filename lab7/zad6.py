import pandas as pd

dane_sprzedazowe = pd.DataFrame({
'Produkt': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A'],
'Ilość': [120, 85, 90, 110, 95, 105, 130, 75, 85, 140],
'Cena_jednostkowa': [10, 15, 12, 10, 15, 12, 10, 15, 12, 10],
'Wartość': [1200, 1275, 1080, 1100, 1425, 1260, 1300, 1125, 1020,
1400]
})

print(dane_sprzedazowe.describe())