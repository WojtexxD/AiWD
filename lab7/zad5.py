import pandas as pd
import numpy as np

dane_lewostronne = pd.Series([90, 85, 82, 81, 80, 79, 75, 70, 65, 50])
dane_symetryczne = pd.Series([50, 60, 65, 70, 75, 80, 85, 90, 95, 100])
dane_prawostronne = pd.Series([50, 55, 60, 65, 70, 75, 76, 78, 85, 95])

for nazwa, dane in [('lewostronne', dane_lewostronne), ('symetryczne', dane_symetryczne), ('prawostronne', dane_prawostronne)]:
    print(f'{nazwa}')
    print('Skosnosc: ', dane.skew())
    print('kurtoza: ', dane.kurtosis())
