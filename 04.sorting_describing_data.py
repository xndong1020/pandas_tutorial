import pandas as pd

df = pd.read_csv("./pokemon_data.csv")

# sort by column name, desc
print(df.sort_values("Name", ascending=False))

# sort by multiple column names, first asc, second desc
"""
     #                     Name Type 1    Type 2  HP  ...  Sp. Atk  Sp. Def  Speed  Generation  Legendary
520  469                  Yanmega    Bug    Flying  86  ...      116       56     95           4      False        
698  637                Volcarona    Bug      Fire  85  ...      135      105    100           5      False        
231  214                Heracross    Bug  Fighting  80  ...       40       95     85           2      False        
232  214  HeracrossMega Heracross    Bug  Fighting  80  ...       40      105     75           2      False        
678  617                 Accelgor    Bug       NaN  80  ...      100       60    145           5      False 
"""
print(df.sort_values(["Type 1", "HP"], ascending=[1, 0])[:5])

