import pandas as pd


ds = pd.read_csv('csvs/sales_by_employee.csv',parse_dates=['Date'])
print(ds)
print(ds.pivot_table(index='Date',aggfunc='sum',values=['Expenses','Revenue']))
print(ds.pivot_table(index='Date',aggfunc='sum',values=['Expenses','Revenue'],columns='Name',margins=True,
                     margins_name='Total',fill_value=0))
print(ds.pivot_table(index='Date',aggfunc=['sum','count'],values=['Revenue','Expenses'],columns='Name'))
print(ds.pivot_table(index='Date',aggfunc={'Revenue':'sum','Expenses':'count'},values=['Revenue','Expenses'],columns='Name'))
print(ds.pivot_table(index=['Name','Date'],values='Revenue'))
new = ds.pivot_table(index='Name',columns='Date',aggfunc='sum',values='Revenue')
print(new.stack())
new = ds.pivot_table(index=['Customer','Name'],columns='Date',aggfunc='sum',values='Revenue')
print(new.unstack())

re = pd.read_csv('csvs/recipes.csv')
re['Ingredients']= re['Ingredients'].str.split(',')
print(re.explode(column='Ingredients'))

vd = pd.read_csv('csvs/video_game_sales.csv')
print(vd.melt(id_vars='Name',value_vars=['NA','EU','JP','Other'],var_name='Region',value_name='sales'))