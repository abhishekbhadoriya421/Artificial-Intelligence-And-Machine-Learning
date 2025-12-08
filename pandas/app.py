import pandas as pd

s = pd.Series([10,20,30,40],index=['a','b','c','d'])

# print((s))

# print(s['l'])

# pandas data frame

data = {
    "name" : ["abhishek","nisha","vivek"],
    "age" : [24,26,22],
    "city" : ["delhi","delhi","delhi"]
}

# df =  pd.DataFrame(data)
# # print(df)
# # print(df[['name','city']])
# print(df.loc[0]) 
# print("\n") 
# print(df.iloc[1])           


# Read Csv

df = pd.read_csv('data.csv')

# print(df.head)

# print(df['name'])

# print(df.loc[0]) 


# print(df.info())
# print(df.describe())

# print(df[df["salary"] > 30000])
print(df.sort_values("salary", ascending=False))

df.to_csv('update.csv',index=False)