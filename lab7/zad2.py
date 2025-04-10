import pandas as pd

dane_symetryczne = pd.Series([10, 20, 30, 40, 50, 60, 70, 80, 90])
dane_skosne = pd.Series([10, 15, 18, 20, 22, 25, 30, 80, 90])

#print('Symetryczne:', dane_symetryczne.mean())
#print('Skosne:', dane_skosne.mean())

#print('Symetryczne:', dane_symetryczne.median())
#print('Skosne:', dane_skosne.median())

#print('Symetryczne:', dane_symetryczne.mode().values)
#print('Skosne:', dane_skosne.mode().values)

for name, data in [('Symetryczne: ', dane_symetryczne), ('Skosne: ', dane_skosne)]:
    print(f'{name}')
    print('Srednia: ', data.mean())
    print('Mediana: ', data.median())
    print('Dominanta: ', data.mode().values)