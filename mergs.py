import pandas as pd

g1 = pd.read_csv('csvs/groups1.csv')
g2 = pd.read_csv('csvs/groups2.csv')
cat = pd.read_csv('csvs/categories.csv')
city = pd.read_csv('csvs/cities.csv',dtype={'Zip':'string'})

groups = pd.concat([g1,g2],ignore_index=True)

print(groups.loc[11])
print(groups)
print(groups.merge(right=cat,how='inner',on='category_id'))
print(groups.merge(right=cat,how='outer',on='category_id'))
print(groups.merge(right=city,how='outer',left_on='city_id',right_on='id'))
یابک میرزا شاهی