import pandas as pd

ep = pd.read_csv('csvs/employees.csv',
                 parse_dates=['Start Date'],
                 usecols=['Gender','Start Date','Salary','Mgmt','Team'],
                 dtype={'Gender':'category'})

ep['Mgmt'] = ep['Mgmt'].astype(bool)
ep['Salary'] = ep['Salary'].fillna(0).astype('int32')
ep['Gender'] = ep['Gender'].astype('category')
ep['Team'] = ep['Team'].astype('category')

# print(ep.info())
# print(ep)


for ep in pd.read_csv('csvs/employees.csv',
                 parse_dates=['Start Date'],
                 usecols=['Gender','Start Date','Salary','Mgmt','Team'],
                chunksize=200):
    print(ep.info())
    print('*'*25)


ep = pd.read_csv('csvs/employees.csv',parse_dates=['Start Date'])

print(ep[ep['First Name'] == 'Maria'])
print(ep[ep['Team'] != 'Finance'])
print(ep[ep['Mgmt'] == True])
