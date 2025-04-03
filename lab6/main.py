from statistics import median

import pandas as pd
from sqlite3 import connect

ceny_paliw = pd.read_excel('data/cena_paliwa11.xlsx')

ceny = pd.read_excel('data/ceny21.xlsx')

daty1 = pd.read_csv('data/date_sale.csv',
                    parse_dates=['Sale_Date'],
                    date_format='%d-%m-%Y')

daty2 = pd.read_csv('data/date_temp.csv')
daty2['Reading_Date'] = pd.to_datetime(daty2['Reading_Date'])

gastro = pd.read_csv('data/gastro21.csv', header=None).T
gastro.columns = ['Rodzaj', 'Rok', 'Wartość']
gastro['Rok'] = gastro['Rok'].astype(int)
gastro["Wartość"] = gastro['Wartość'].astype(int)

handel = pd.read_excel('data/handel25.xlsx')

kurs = pd.read_csv('data/kurs4.csv', sep=';', decimal=',')

conn = connect('data/lab_readings.db')
query = 'select * from readings'
odczyty = pd.read_sql(query, conn)
odczyty['measurement_time'] = pd.to_datetime(odczyty['measurement_time'])

pogoda = pd.read_csv('data/pogoda25.csv', sep=';')

data1 = connect('data/sales_data2.db')
query = 'select * from sales_data'
sprzedaz1 = pd.read_sql(query, data1, parse_dates=['date'])
# odczyty1 = pd.read_sql(query, data1)
# odczyty1['date'] = pd.to_datetime(odczyty1['date'])


data2 = connect('data/sales_data3.db')
query = 'select * from sales'
sprzedaz2 = pd.read_sql(query, data2, parse_dates=['sale_date'])

sport = pd.read_csv('data/sport2.csv', sep='#')

wynagrodzenie = pd.read_csv('data/wynagrodzenia21.csv', sep=';', decimal=',')
# wynagrodzenie = wynagrodzenie.melt(id_vars='Województwo', var_name='Rok', value_name='Wynagrodzenie')

wynagrodzenie = wynagrodzenie.rename(columns=lambda x: f'wyn_{x}' if x.isdigit() else x)
wynagrodzenie_long = pd.wide_to_long(wynagrodzenie, stubnames='wyn', i='Województwo', j='Rok', sep='_')
wynagrodzenie_long = wynagrodzenie_long.reset_index().rename(columns={'wyn': 'Wynagrodzenie'})
