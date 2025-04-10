from operator import index

import pandas as pd
from openpyxl.utils.datetime import to_excel

nobel = pd.read_json('csvs/prize.json')

second = nobel.loc[2,'prizes']

print(pd.json_normalize(second,record_path='laureates',meta=['year','category']))

def add_laureates_key(entry):
    entry.setdefault('laureates',[])

nobel['prizes'].apply(add_laureates_key)
winner = pd.json_normalize(nobel['prizes'],record_path='laureates',meta=['year','category'])
# winner.head().to_json('new_prize.json',orient = 'records')

baby = pd.read_csv('csvs/Popular_Baby_Names.csv')
baby.head().to_csv('New_baby.csv',index=False,columns=["Gender","Child's First Name"])

single = pd.read_excel(io='csvs/Single Worksheet.xlsx' ,usecols=['City','First Name','Last Name'],index_col='City')
print(single)

single = pd.read_excel('csvs/Multiple Worksheets.xlsx',sheet_name=2)
print(single)

single = pd.read_excel('csvs/Multiple Worksheets.xlsx',sheet_name=None)
print(single)

baby = pd.read_csv('csvs/Popular_Baby_Names.csv')
girls = baby[baby['Gender'] == 'FEMALE']
boys = baby[baby['Gender'] == 'Male']
with pd.ExcelWriter('New_baby.xlsx') as writer :
    girls.to_excel(excel_writer=writer,sheet_name='Girls',index=False)
    boys.to_excel(excel_writer=writer, sheet_name='Boys',index=False)