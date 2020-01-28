import pandas as pd
import json
import ast
df=pd.read_csv('Data.csv',encoding = "ISO-8859-1")
Condition_mercari=['New With Tags','New Without tags','']
for i in range(len(df)):
    data=df['Dict Data Multifield'][i]
    # res = json.loads(data)
    res = ast.literal_eval(data)
    condition=res.get(" Condition"," ")
    type=res.get(' Type',"Null")
    print(condition)
    print(type)