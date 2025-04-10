import pandas as pd

sprzedaz = pd.DataFrame({
'Produkt': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B'],
'Region': ['Wschód', 'Wschód', 'Wschód', 'Zachód', 'Zachód',
'Zachód', 'Północ', 'Północ'],
'Ilość': [120, 85, 90, 110, 95, 105, 130, 75],
'Wartość': [1200, 1275, 1080, 1100, 1425, 1260, 1300, 1125]
})

print(sprzedaz.groupby('Region').agg(
    {'Ilość': ['sum', 'std', 'mean'],
     'Wartość': ['var', 'median', 'max']}))

    