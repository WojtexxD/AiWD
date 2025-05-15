import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#x = ['Fakt', 'Super Express', 'Gazeta Wyborcza', 'Rzeczpospolita']
#y = [130000, 70000, 40000, 17000]
#c = ['aquamarine', 'peachpuff', 'lightsteelblue', 'plum']
#plt.bar(x,y,color=c, alpha=0.5)
#plt.xticks(x, rotation=45, ha='right')
#plt.title('Wyniki sprzedaży dzienników ogólnopolskich za 1Q2023')
#plt.tight_layout()

data={'Gazeta':['Fakt','Super Express', 'Gazeta Wyboracza', 'Rzeczpospolita'],
      'Sprzedaż':[130000,70000,40000,17000]}
df = pd.DataFrame(data)
y_pos = np.arange(len(df))
kolory = {'Fakt':'mediumaquamarine','Super Express':'peachpuff', 'Gazeta Wyboracza':'lightsteelblue', 'Rzeczpospolita':'plum'}
colors_list = [kolory[kat] for kat in df['Gazeta']]
fig, ax = plt.subplots(figsize=(8,6))
ax.bar(y_pos,df['Sprzedaż'],color=colors_list,alpha=0.8)
ax.set_title('Wyniki sprzedaży dzienników ogólnopolskich za 1Q2023')
ax.set_xticks(y_pos,df['Gazeta'], rotation=45)
fig.tight_layout()
plt.savefig('zad2.png', format='png')
plt.show()