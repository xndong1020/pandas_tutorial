### Loading the data into Pandas (CSVs, Excel, TXTs, etc.)

1. read csv

```py
df = pd.read_csv("./pokemon_data.csv")
```

2. read excel
   you need to install xlrd

```
pipenv install xlrd==1.2.0
```

then in your code

```py
df_xlsx = pd.read_excel("./pokemon_data.xlsx")
```

3. read txt

```py
# in 'pokemon_data.txt', columns are separated by tab, so we specify the delimiter as `\t`
df = pd.read_csv("./pokemon_data.txt", delimiter="\t")
```

### basics (head, tail, columns)

```py
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

```

### read rows using iloc & loc

```py
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

```

### iteration over rows

```py
import pandas as pd

df = pd.read_csv("./pokemon_data.csv")

# loop through a data frame
for index, row in df.iterrows():
    print(index, row)

```

### Sorting

```py
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
```

### Making changes (add column(s), drop columns(s), rearrange column(s) )

```py
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

```

### save to disk

```py
# save to disk, index=False to remove the pandas index column
df.to_csv("modified.csv", index=False)

```

save to excel

You have to install 'openpyxl' first

```
pipenv install openpyxl
```

```py
# save as excel.
df.to_excel("modified.xlsx", index=False)
```

save as .txt file, use 'tab' as separator

```py
# save to disk, index=False to remove the pandas index column
df.to_csv("modified.txt", index=False, sep="\t")
```

### Advanced filtering (contains, regex)

```py
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

```

### Conditional Changes

```py
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
```

### Groupby

```py
import pandas as pd

df = pd.read_csv("./pokemon_data.csv")

# groupby 'Type 1'
print(df.groupby(["Type 1"]).mean().sort_values(["HP"], ascending=False))

print(df.groupby(["Type 1"]).count())
"""
                  #         HP      Attack     Defense    Sp. Atk    Sp. Def       Speed  Generation  Legendary
Type 1
Bug       334.492754  56.884058   70.971014   70.724638  53.869565  64.797101   61.681159    3.217391   0.000000
Electric  363.500000  59.795455   69.090909   66.295455  90.022727  73.704545   84.500000    3.272727   0.090909
Ghost     486.500000  64.437500   73.781250   81.187500  79.343750  76.468750   64.343750    4.187500   0.062500
Steel     442.851852  65.222222   92.703704  126.370370  67.518519  80.629630   55.259259    3.851852   0.148148
Rock      392.727273  65.363636   92.863636  100.795455  63.340909  75.477273   55.909091    3.454545   0.090909
Dark      461.354839  66.806452   88.387097   70.225806  74.645161  69.516129   76.161290    4.032258   0.064516
Poison    251.785714  67.250000   74.678571   68.821429  60.428571  64.392857   63.571429    2.535714   0.000000
Grass     344.871429  67.271429   73.214286   70.800000  77.500000  70.428571   61.928571    3.357143   0.042857
Fighting  363.851852  69.851852   96.777778   65.925926  53.111111  64.703704   66.074074    3.370370   0.000000
Fire      327.403846  69.903846   84.769231   67.769231  88.980769  72.211538   74.442308    3.211538   0.096154
Psychic   380.807018  70.631579   71.456140   67.684211  98.403509  86.280702   81.491228    3.385965   0.245614
Flying    677.750000  70.750000   78.750000   66.250000  94.250000  72.500000  102.500000    5.500000   0.500000
Ice       423.541667  72.000000   72.750000   71.416667  77.541667  76.291667   63.458333    3.541667   0.083333
Water     303.089286  72.062500   74.151786   72.946429  74.812500  70.517857   65.964286    2.857143   0.035714
Ground    356.281250  73.781250   95.750000   84.843750  56.468750  62.750000   63.906250    3.156250   0.125000
Fairy     449.529412  74.117647   61.529412   65.705882  78.529412  84.705882   48.588235    4.117647   0.058824
Normal    319.173469  77.275510   73.469388   59.846939  55.816327  63.724490   71.551020    3.051020   0.020408
Dragon    474.375000  83.312500  112.125000   86.375000  96.843750  88.843750   83.031250    3.875000   0.375000
"""

# you can count the group size by adding a temp column 'count'

df["count"] = 1

"""
Type 1
Bug        69    69      52   69      69       69       69       69     69          69         69     69
Dark       31    31      21   31      31       31       31       31     31          31         31     31
Dragon     32    32      21   32      32       32       32       32     32          32         32     32
Electric   44    44      17   44      44       44       44       44     44          44         44     44
Fairy      17    17       2   17      17       17       17       17     17          17         17     17
Fighting   27    27       7   27      27       27       27       27     27          27         27     27
Fire       52    52      24   52      52       52       52       52     52          52         52     52
Flying      4     4       2    4       4        4        4        4      4           4          4      4
Ghost      32    32      22   32      32       32       32       32     32          32         32     32
Grass      70    70      37   70      70       70       70       70     70          70         70     70
Ground     32    32      19   32      32       32       32       32     32          32         32     32
Ice        24    24      11   24      24       24       24       24     24          24         24     24
Normal     98    98      37   98      98       98       98       98     98          98         98     98
Poison     28    28      13   28      28       28       28       28     28          28         28     28
Psychic    57    57      19   57      57       57       57       57     57          57         57     57
Rock       44    44      35   44      44       44       44       44     44          44         44     44
Steel      27    27      22   27      27       27       27       27     27          27         27     27
Water     112   112      53  112     112      112      112      112    112         112        112    112
"""

print(df.groupby(["Type 1"]).count().sort_values("count", ascending=False)["count"])
"""
Type 1
Water       112
Normal       98
Grass        70
Bug          69
Psychic      57
Fire         52
Electric     44
Rock         44
Ghost        32
Ground       32
Dragon       32
Dark         31
Poison       28
Fighting     27
Steel        27
Ice          24
Fairy        17
Flying        4
Name: count, dtype: int64
"""

```

### Working with large amount of data (chunksize)

```py
import pandas as pd

# let's assume we have a large amount of data in the data source, if you load all data at once, then you will need a lot of memory
# what you can do is, you can load data by chunks, and do groupby on those chunks, then aggregate the results

# load 5 rows at a time
for df in pd.read_csv("./pokemon_data.csv", chunksize=50):
    print(df)

```
