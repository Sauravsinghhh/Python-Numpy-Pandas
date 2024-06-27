import pandas as pd

data = {
    'Name': ['Saurav', 'Uttam', 'Rashmi','Hardik'],
    'Age': [25, 30, 35,40],
    'City': ['New York', 'Los Angeles', 'Chicago','Toronto']
}

df = pd.DataFrame(data)
print(df)

data = [
    ['Saurav', 25, 'New York'],
    ['Uttam', 30, 'Los Angeles'],
    ['Rashmi', 35, 'Chicago'],
    ['Hardik', 40, 'Toronto']
]

df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print(df)
