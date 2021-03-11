import pandas as pd

df = pd.read_csv("./pokemon_data.csv")

# add a new column 'Total', for ranking pokemon
df["Total"] = df["HP"] + df["Attack"] + df["Defense"] + df["Speed"]


"""
       #                   Name   Type 1    Type 2   HP  ...  Sp. Def  Speed  Generation  Legendary  Total
424  383  GroudonPrimal Groudon   Ground      Fire  100  ...       90     90           3       True    530
163  150    MewtwoMega Mewtwo X  Psychic  Fighting  106  ...      100    130           1       True    526
313  289                Slaking   Normal       NaN  150  ...       65    100           3      False    510
426  384  RayquazaMega Rayquaza   Dragon    Flying  105  ...      100    115           3       True    500
711  646     KyuremBlack Kyurem   Dragon       Ice  125  ...       90     95           5       True    490
"""
print(df.sort_values("Total", ascending=False))

# add column using iloc, for every rows, add values from column 5 to 10, then sum value horizontally
df["Total All"] = df.iloc[:, 4:10].sum(axis=1)

"""
       #                   Name   Type 1    Type 2   HP  ...  Speed  Generation  Legendary  Total  Total All
426  384  RayquazaMega Rayquaza   Dragon    Flying  105  ...    115           3       True    500        780       
164  150    MewtwoMega Mewtwo Y  Psychic       NaN  106  ...    140           1       True    466        780       
163  150    MewtwoMega Mewtwo X  Psychic  Fighting  106  ...    130           1       True    526        780       
422  382    KyogrePrimal Kyogre    Water       NaN  100  ...     90           3       True    430        770       
424  383  GroudonPrimal Groudon   Ground      Fire  100  ...     90           3       True    530        770
"""
print(df.sort_values("Total All", ascending=False))

# drop columns
print(df.drop(columns=["Total"]))


# re-order the data frame, put the 'Total All' column in the middle
cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
print(df.head(3))

# save to disk, index=False to remove the pandas index column
df.to_csv("modified.txt", index=False, sep="\t")

