import pandas as pd

dane_studentow = pd.DataFrame({
'Student': ['Anna', 'Bartek', 'Celina', 'Dawid', 'Ewa', 'Filip',
'Gosia', 'Hubert'],
'Matematyka': [85, 90, 78, 92, 88, 76, 94, 85],
'Fizyka': [76, 88, 90, 75, 82, 84, 91, 76],
'Informatyka': [92, 85, 88, 95, 80, 75, 89, 92]
})

print('Średnia Matematyka: ', dane_studentow['Matematyka'].mean())
print('Średnia Fizyka: ', dane_studentow['Fizyka'].mean())
print('Średnia Informatyka: ', dane_studentow['Informatyka'].mean())
print('Mediana Matematyka: ', dane_studentow['Matematyka'].median())
print('Mediana Fizyka: ', dane_studentow['Fizyka'].median())
print('Mediana Informatyka: ', dane_studentow['Informatyka'].median())
print('Mediana Matematyka: ', dane_studentow['Matematyka'].mode().values)
print('Mediana Fizyka: ', dane_studentow['Fizyka'].mode().values)
print('Mediana Informatyka: ', dane_studentow['Informatyka'].mode().values)


