import pandas as pd
import re

df = pd.read_csv("./pokemon_data.csv")

df_grass = df.loc[df["Type 1"] == "Grass"]

print(df_grass)

# multiple conditions. '&' for 'and', '|' for 'or'
df_grass = df.loc[
    (df["Type 1"] == "Grass") & (df["Type 2"] == "Poison") & (df["HP"] >= 70)
]

"""
       #                   Name Type 1  Type 2   HP  ...  Sp. Atk  Sp. Def  Speed  Generation  Legendary
2      3               Venusaur  Grass  Poison   80  ...      100      100     80           1      False
3      3  VenusaurMega Venusaur  Grass  Poison   80  ...      122      120     80           1      False
50    45              Vileplume  Grass  Poison   75  ...      110       90     50           1      False
77    71             Victreebel  Grass  Poison   80  ...      100       70     70           1      False
652  591              Amoonguss  Grass  Poison  114  ...       85       80     30           5      False

[5 rows x 12 columns]
"""
print(df_grass)

# filter out any Name which does NOT contains 'mega'
df_grass = df_grass.loc[~(df["Name"].str.contains("Mega"))]

"""
       #        Name Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
2      3    Venusaur  Grass  Poison   80      82       83      100      100     80           1      False
50    45   Vileplume  Grass  Poison   75      80       85      110       90     50           1      False
77    71  Victreebel  Grass  Poison   80     105       65      100       70     70           1      False
652  591   Amoonguss  Grass  Poison  114      85       70       85       80     30           5      False
"""
print(df_grass)

# you can use regex for pattern matching, find all fire/grass type, case insensitive
df_grass = df.loc[df["Type 1"].str.contains("fire|grass", flags=re.I, regex=True)]

print(df_grass)

# find all names starts with pi
df_grass = df.loc[df["Name"].str.contains("^pi[a-z]*", flags=re.I, regex=True)]

"""
       #                 Name    Type 1    Type 2   HP  ...  Sp. Atk  Sp. Def  Speed  Generation  Legendary
20    16               Pidgey    Normal    Flying   40  ...       35       35     56           1      False        
21    17            Pidgeotto    Normal    Flying   63  ...       50       50     71           1      False        
22    18              Pidgeot    Normal    Flying   83  ...       70       70    101           1      False        
23    18  PidgeotMega Pidgeot    Normal    Flying   83  ...      135       80    121           1      False        
30    25              Pikachu  Electric       NaN   35  ...       50       50     90           1      False        
136  127               Pinsir       Bug       NaN   65  ...       55       70     85           1      False        
137  127    PinsirMega Pinsir       Bug    Flying   65  ...       65       90    105           1      False        
186  172                Pichu  Electric       NaN   20  ...       35       35     60           2      False        
219  204               Pineco       Bug       NaN   50  ...       35       35     15           2      False        
239  221            Piloswine       Ice    Ground  100  ...       60       60     50           2      False        
438  393               Piplup     Water       NaN   53  ...       61       56     40           4      False        
558  499              Pignite      Fire  Fighting   90  ...       70       55     55           5      False        
578  519               Pidove    Normal    Flying   50  ...       36       30     43           5      False        

[13 rows x 12 columns]
"""
print(df_grass)

# note the first column is the original dataframe index. we can reset the index
# df_grass = df_grass.reset_index()

"""
index    #                   Name Type 1  Type 2   HP  ...  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
0      2    3               Venusaur  Grass  Poison   80  ...       83      100      100     80           1      False
1      3    3  VenusaurMega Venusaur  Grass  Poison   80  ...      123      122      120     80           1      False
2     50   45              Vileplume  Grass  Poison   75  ...       85      110       90     50           1      False
3     77   71             Victreebel  Grass  Poison   80  ...       65      100       70     70           1      False
4    652  591              Amoonguss  Grass  Poison  114  ...       70       85       80     30           5      False

[5 rows x 13 columns]
"""
# print(df_grass)

# You can see the index is reset, however it keeps the old index, next to the new index, we can drop it by adding a 'drop' flag when reseting the index
# df_grass = df_grass.reset_index(drop=True)

"""
     #                   Name Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
0    3               Venusaur  Grass  Poison   80      82       83      100      100     80           1      False 
1    3  VenusaurMega Venusaur  Grass  Poison   80     100      123      122      120     80           1      False 
2   45              Vileplume  Grass  Poison   75      80       85      110       90     50           1      False 
3   71             Victreebel  Grass  Poison   80     105       65      100       70     70           1      False 
4  591              Amoonguss  Grass  Poison  114      85       70       85       80     30           5      False 
"""
# print(df_grass)

# and if you don't want to create a new array, just want to change the value in the data frame, then you can pass in 'inplace=True'

df_grass.reset_index(drop=True, inplace=True)

"""
     #                   Name Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
0    3               Venusaur  Grass  Poison   80      82       83      100      100     80           1      False 
1    3  VenusaurMega Venusaur  Grass  Poison   80     100      123      122      120     80           1      False 
2   45              Vileplume  Grass  Poison   75      80       85      110       90     50           1      False 
3   71             Victreebel  Grass  Poison   80     105       65      100       70     70           1      False 
4  591              Amoonguss  Grass  Poison  114      85       70       85       80     30           5      False 
"""
# print(df_grass)

