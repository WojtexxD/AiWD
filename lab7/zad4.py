import pandas as pd

pomiary = pd.DataFrame({
'Próbka': ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'],
'Wynik1': [45, 47, 49, 51, 46, 48, 50, 52],
'Wynik2': [120, 150, 110, 190, 200, 115, 140, 180]
})

#max = pomiary['Wynik1'].max()
#min = pomiary['Wynik1'].min()
#print('Rozstęp: ', max-min)
#odchylenie_standardowe = pomiary['Wynik1'].std()
#print('Odchylenie standardowe: ', odchylenie_standardowe)
#wariancja = pomiary['Wynik1'].var()
#print('Wariancja: ', wariancja)
#max = pomiary['Wynik2'].max()
#min = pomiary['Wynik2'].min()
#print('Rozstęp: ', max-min)
#odchylenie_standardowe = pomiary['Wynik2'].std()
#print('Odchylenie standardowe: ', odchylenie_standardowe)
#wariancja = pomiary['Wynik2'].var()
#print('Wariancja: ', wariancja)

for nazwa_kolumny in ('Wynik1', 'Wynik2'):
    print(f'{nazwa_kolumny}')
    print('Rozstep: ', pomiary[nazwa_kolumny].max()-pomiary[nazwa_kolumny].min())
    print('Odchylenie standardowe: ', pomiary[nazwa_kolumny].std())
    print('Wariancja: ', pomiary[nazwa_kolumny].var())