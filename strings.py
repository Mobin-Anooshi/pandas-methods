import pandas as pd
import numpy as np


# cg = pd.read_csv('csvs/chicago_food_inspections.csv')
# cg['Name'] = cg['Name'].str.lower().values
# cg['Name'] = cg['Name'].str.strip()
# cg['Name'] = cg['Name'].str.lower()
# print(cg['Name'].str.strip().values)
# print(cg['Name'].str.upper().values)
# print(cg['Name'].str.strip().values)
# cg = cg.dropna(subset=['Risk'])
# cg = cg.replace(to_replace='All',value='Risk 4 (Extreme)')
# print(cg['Risk'].unique())
# print(cg['Risk'].str.slice(5,6))
# print(cg['Risk'].str[5:6])
# print(cg)
# print(cg[cg['Name'].str.lower().str.contains('pizza')])
# print(cg[cg['Name'].str.lower().str.startswith('pizza')])
# print(cg[cg['Name'].str.lower().str.endswith('pizza')])



cg = pd.read_csv('csvs/customers.csv')
print(cg['Address'].str.replace('^\d+','*',regex=True))
print(cg['Name'].str.split(pat=' ',n=1).str.get(0))
print(cg['Name'].str.split(pat=' ',n=1))
print(cg['Name'].str.split(pat=' ',n=1,expand=True))
cg[['First Name','Last Name']] = cg['Name'].str.split(' ',n=1,expand=True)
cg = cg.drop(labels='Name',axis='columns')
print(cg)
