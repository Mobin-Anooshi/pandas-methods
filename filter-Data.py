import pandas as pd
import numpy as np


ep = pd.read_csv('csvs/employees.csv',parse_dates=['Start Date'])

print(ep[ep['First Name'] == 'Maria'])
print(ep[ep['Team'] !='Finance'])

is_female = ep['Gender'] == 'Female'
is_finance = ep['Team'] == 'Finance'
print(ep[is_finance & is_female]) # And
print(ep[is_finance | is_female]) # Or
print(ep[~is_finance & ~is_female]) # Not

high_salary = ep['Salary'] > 100000
print(ep[high_salary])

print(ep[ep['Team'].ne('Finance')])
print(ep[ep['Team'].eq('Finance')])
print(ep[ep['Salary'].lt(100000)])
print(ep[ep['Team'].le(100000)])
print(ep[ep['Team'].isin(['Marketing','Product','Finance'])])
print(ep[ep['Salary'].between(left=100000,right=120000)])
print(ep[ep['Team'].isnull()])
print(ep[ep['Team'].notnull()])
print(ep.dropna())
print(ep.dropna(how='all'))
print(ep.dropna(subset=['Gender','Start Date']))
print(ep.dropna(thresh=4))
print(ep[~ep['Team'].duplicated()])