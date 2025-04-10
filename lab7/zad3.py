import pandas as pd

ceny_produktow = pd.DataFrame({
'Produkt': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
'Cena': [25, 35, 40, 45, 50, 55, 60, 75, 90, 120]
})

#kwartyl1 = ceny_produktow['Cena'].quantile(0.25)
#kwartyl2 = ceny_produktow['Cena'].quantile(0.50)
#kwartyl3 = ceny_produktow['Cena'].quantile(0.75)
#print('\n', kwartyl1, '\n', kwartyl2, '\n', kwartyl3)

kwartyle = ceny_produktow['Cena'].quantile([0.25,0.50,0.75])
print('\n Kwartyle \n', kwartyle)
print('Rozstep miedzykwartylowy (InterQuartile Range): ', kwartyle[0.75]-kwartyle[0.25])