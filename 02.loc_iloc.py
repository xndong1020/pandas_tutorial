import pandas as pd

df = pd.read_csv("./pokemon_data.csv")

# read specific rows, using iloc, which stands for integer location
"""
#                   2
Name          Ivysaur
Type 1          Grass
Type 2         Poison
HP                 60
Attack             62
Defense            63
Sp. Atk            80
Sp. Def            80
Speed              60
Generation          1
Legendary       False
Name: 1, dtype: object
"""
print(df.iloc[1])  # second row

# read multiple rows using iloc
"""
   #                   Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
1  2                Ivysaur  Grass  Poison  60      62       63       80       80     60           1      False    
2  3               Venusaur  Grass  Poison  80      82       83      100      100     80           1      False    
3  3  VenusaurMega Venusaur  Grass  Poison  80     100      123      122      120     80           1      False  
"""
print(df.iloc[1:4])  # 2-4 rows

# use iloc to read a specific location (R, C), meaning (Row, Column)

print(df.iloc[2, 1])  # row 3, second column, Venusaur

"""
  Type 1  Type 2
1  Grass  Poison
2  Grass  Poison
3  Grass  Poison
"""
print(df.iloc[1:4, 2:4])  # row 2-4, column 2-3

# compare loc vs iloc. loc is based on textual/numerical information, iloc is based on integer index.

# find the first 5 pokeman who has Type 1 equals to "Fire"
"""
   #                       Name Type 1  Type 2  HP  ...  Sp. Atk  Sp. Def  Speed  Generation  Legendary
4  4                 Charmander   Fire     NaN  39  ...       60       50     65           1      False
5  5                 Charmeleon   Fire     NaN  58  ...       80       65     80           1      False
6  6                  Charizard   Fire  Flying  78  ...      109       85    100           1      False
7  6  CharizardMega Charizard X   Fire  Dragon  78  ...      130       85    100           1      False
8  6  CharizardMega Charizard Y   Fire  Flying  78  ...      159      115    100           1      False
"""
print(df.loc[df["Type 1"] == "Fire"][:5])
