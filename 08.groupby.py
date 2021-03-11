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
