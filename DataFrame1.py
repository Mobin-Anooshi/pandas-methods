import pandas as pd
import numpy as np


df = pd.DataFrame(data={
    'City':['Tehran','London','Paris'],
    'Country':['Iran','England','France'],
    'Population':['85000000','70000000','60000000']
})
print(df)
print(df.transpose()) # change colum to row

r = np.random.randint(1,100,[3,5])
df = pd.DataFrame(data=r,index=['one','two','three'],columns=['a','b','c','d','e'])
print(df)

nba = pd.read_csv('csvs/nba.csv',parse_dates=['Birthday'],index_col='Name')
print(nba.dtypes.value_counts())
print(nba.dtypes)
print(nba.index)
print(nba.shape)
print(nba.size)
print(nba.count())
print(nba.count().sum())
print(nba.head())
print(nba.nunique())
print(nba.nlargest(2,'Salary'))
print(nba.nsmallest(3,'Salary'))
print(nba.sum(numeric_only=True))
print(nba.sort_values(by=['Position','Birthday'],ascending=[True,False]))
print(nba.sort_index(axis='columns')) # row or columns
# print(nba.set_index(keys='Name')) # or we can set index in base : index_col=['Name']
print(nba['Salary'])
print(nba[ ['Birthday','Salary'] ])
print(nba.select_dtypes(include='object'))
print(nba.select_dtypes(exclude='object'))
print(nba.loc[['LeBron James','Paul George']])
print(nba.sort_index().loc['Zach LaVine':'Zylan Cheatham'])
print(nba.iloc[2:7])
print(nba.loc['Paul George','Salary'])
print(nba.at['Paul George','Birthday'])
print(nba.iat[14,2])
print(nba.columns)
nba.columns = ['Team','Position','Birthday','pay'] # rename columns
print(nba)
nba.rename(columns={'Salary':'Pay'})
print(nba)
nba.rename(index={'Paul Gorge':'Mobin Anooshi'}) #raname index objects
print(nba.reset_index().set_index('Team'))