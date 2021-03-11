import pandas as pd

# let's assume we have a large amount of data in the data source, if you load all data at once, then you will need a lot of memory
# what you can do is, you can load data by chunks, and do groupby on those chunks, then aggregate the results

results_df = pd.DataFrame()

# load 5 rows at a time
for df in pd.read_csv("./pokemon_data.csv", chunksize=50):
    df["count"] = 1
    results = df.groupby(["Type 1"]).count().sort_values("count", ascending=False)
    results_df = pd.concat([results_df, results])

print(results_df.groupby(["count"]).sum().sort_values("Legendary", ascending=False))

