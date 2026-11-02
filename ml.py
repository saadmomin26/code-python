import pandas as pd
data ={
    "name":['pavan','kapil','lalit','ishan','om'],
    'age':[25,None,44,23,None],
    'salary':[50000,6000,7000,None,None]

}
df =pd.DataFrame(data)
print("original dataframe")
print(df)

print(df.isnull().sum())
df_drop=df.dropna()
print(df_drop)