import pandas as pd

df = pd.read_csv("./pokemon_data.csv")

# read column names
"""
Index(['#', 'Name', 'Type 1', 'Type 2', 'HP', 'Attack', 'Defense', 'Sp. Atk',
       'Sp. Def', 'Speed', 'Generation', 'Legendary'],
      dtype='object')
"""
print(df.columns)

# read a specific column
"""
0                Bulbasaur
1                  Ivysaur
2                 Venusaur
3    VenusaurMega Venusaur
4               Charmander
Name: Name, dtype: object
"""
print(df["Name"].head(5))

# df.Name is the same as df["Name"], but the dot syntax doesn't work for 2 words.
print(df.Name.head(5))

# you can read multiple columns
print(df[["Name", "Type 1"]][:5])
