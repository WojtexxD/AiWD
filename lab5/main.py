import pandas as pd
import numpy as np

# zad1===================================================
zad1 = pd.Series([15, 28, 33, 47, 52, 61])
print(zad1.to_numpy())
print(type(zad1.to_numpy()))
print(zad1.to_numpy()[zad1>40])

# zad2===================================================
zad2 = pd.Series({'jabłka': 120, 'gruszki': 85, 'śliwki':95, 'banany': 140})
zad2.name = "Owoce"
zad2.index.name = "Produkt"
print(zad2)
print(zad2["gruszki"])
zad2["gruszki"]=110
print(zad2["gruszki"])
zad2 = zad2*2
print(zad2)

# zad3===================================================
d = {'klucz1': 50, 'klucz2': 100, 'klucz3': 150}
k = ['klucz0', 'klucz2', 'klucz3', 'klucz4']
zad3 = pd.Series(d, index=k)
print(zad3)
# klucz0 i klucz4 mają wartości NaN dlatego, że słownik nie posiada tych kluczy a indexy mają takie powstać a ich nie ma więc wypisuje nam NaN
zad3.name = "Wartości"
zad3.index.name = "Klucz"

# zad4===================================================
data = {'Student': ['Anna', 'Bartek', 'Celina', 'Daniel'],
        'Matematyka': [4.5, 3.5, 5.0, 3.0],
        'Fizyka': [4.0, 4.5, 3.5, 3.0],
        'Informatyka': [5.0, 3.0, 4.5, 4.0]}
df_zad4 = pd.DataFrame(data, index = data['Student'])
df_zad4.drop("Student", axis=1, inplace=True)
print(df_zad4)
print(df_zad4.shape)
print(df_zad4.index)
print(df_zad4.columns)
df_zad4.info()
print(df_zad4.count())

# zad5===================================================
data = {'Kraj': ['Polska', 'Niemcy', 'Francja'],
        'Stolica': ['Warszawa', 'Berlin', 'Paryż'],
        'Populacja': [38000000, 83000000, 67000000]}
df_zad5 = pd.DataFrame(data)
print(df_zad5.iloc[0:1, 0:1])
print(df_zad5.iloc[2:3, :])
print(df_zad5.loc[0:3, ["Stolica"]])
print(df_zad5.loc[[1], ["Stolica"]])

# zad6===================================================
data = {'Region': ['Północ', 'Południe', 'Wschód', 'Zachód', 'Północ',
        'Południe'],
        'Produkt': ['A', 'A', 'A', 'A', 'B', 'B'],
        'Sprzedaż': [150, 200, 130, 180, 220, 170]}
df = pd.DataFrame(data)

print(df.loc[:, ["Sprzedaż"]])
print(df.loc[:, "Sprzedaż"][df.loc[:, "Sprzedaż"] > 180])

# zad7===================================================
data = {
            'Region': ['North', 'South', 'East', 'West', 'North', 'South'],
            'Product': ['Electronics', 'Furniture', 'Clothing', 'Electronics',
            'Furniture', 'Clothing'],
            'Sales_Channel': ['Online', 'Retail', 'Online', 'Wholesale',
            'Retail', 'Online'],
            'Units_Sold': [120, 80, 200, 150, 90, 300],
            'Revenue': [60.5, 45.0, 35.0, 70.0, 50.5, 55.0],
            'Profit': [15.2, 12.0, 8.5, 20.5, 13.2, 10.0]
        }
sales_df = pd.DataFrame(data)
print(sales_df.loc[:, 'Revenue'])
print(sales_df.iloc[:, :][sales_df.loc[:, "Profit"] > 15.0])    # df[df["Profit]>15.0]
print(sales_df.iloc[:, :][sales_df.loc[:, "Profit"] > 15.0]["Revenue"]) # df[df["Profit]>15.0]["Revenue"]
print(sales_df[sales_df["Revenue"] == sales_df["Revenue"].max()])
print(sales_df.iloc[sales_df["Revenue"].idxmax()])
sales_df["Revenue_per_Unit"] = sales_df["Revenue"]/sales_df["Units_Sold"]
print(sales_df)

# zad????===================================================
df = pd.read_csv('imiona.csv', header=None, nrows=2)
print(df)