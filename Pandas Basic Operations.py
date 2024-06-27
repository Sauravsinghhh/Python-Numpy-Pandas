import pandas as pd

data = {
    'Name': ['Saurav', 'Uttam', 'Rashmi','Hardik','Japjot','Sakshi','Tarun','Vansh','Piyush'],
    'Age': [25, 30, 35, 40, 23, 23, 45, 32, 54],
    'City': ['New York', 'Los Angeles', 'Chicago','Toronto','New Jersey','Delhi','Califronia','Brampton','Chennai']
}

df = pd.DataFrame(data)
print(df)

print(df.head(3))  
print(df.head(2))  

print(df.tail())
print(df.tail(2))  

print(df.info())

print(df.describe())

print(df['Name'])

print(df[['Name', 'Age']])

print(df.iloc[0])
print(df.iloc[1:3]) 

print(df.loc[0])
print(df.loc[df['Age'] > 30]) 

print(df.at[0, 'Name'])

filtered_df = df[df['Age'] > 30]
print(filtered_df)

