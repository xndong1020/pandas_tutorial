import pandas as pd

df = pd.read_csv("./pokemon_data.csv")

# loop through a data frame
for index, row in df.iterrows():
    print(index, row)

