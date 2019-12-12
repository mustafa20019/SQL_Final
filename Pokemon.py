import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv('pokemon_data.csv')
df['TotalPower'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp.Atk'] + df['Sp.Def'] + df['Speed']
#top_df = df.loc[(df['TotalPower'] > 700)]
#print(new_df)
#df.to_csv('modified.csv', index=False) saves file
new_df = df.groupby(['Type1']).mean().sort_values('TotalPower', ascending=False)

print(new_df)
plt.bar(df["Type1"],df["TotalPower"])
plt.xlabel('Elements')
plt.ylabel('TotalPower')
plt.title ('Strongest Element in Pokemon')
plt.show()
new_df.to_csv('modified.csv', index=False)
