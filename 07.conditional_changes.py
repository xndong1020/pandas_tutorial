import pandas as pd

df = pd.read_csv("./pokemon_data.csv")

# if Type 1 is 'Fire', then replace its Type 1 value to 'Flammer'
df.loc[df["Type 1"] == "Fire", "Type 1"] = "Flammer"

print(df.loc[df["Type 1"] == "Flammer"])

# if Type 1 is 'Flammer', then change 'Legendary' value to 'True'
df.loc[df["Type 1"] == "Flammer", "Legendary"] = True

print(df.loc[df["Type 1"] == "Flammer"])

# change multiple columns
df.loc[df["Type 1"] == "Flammer", ["Generation", "Legendary"]] = [2, False]

print(df.loc[df["Type 1"] == "Flammer"])
