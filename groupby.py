import pandas as pd

food_data = {
    "Item":['Banana','Cucumber','Orange','Tomato','Watermelon'],
    "Type":['Fruit','Vegetable','Fruit','Vegetable','Fruit'],
    "Price":[0.99,1.25,0.25,0.33,3.00]
}

supermarket = pd.DataFrame(data=food_data)
# print(supermarket)
# g = supermarket.groupby(by='Type')
# print(g.mean(numeric_only=True))
# print(g.get_group('Fruit'))
# print(g.get_group('Fruit').mean(numeric_only=True))

ft = pd.read_csv('csvs/fortune1000.csv')
# a = ft[ft['Sector'] == 'Technology'].mean(numeric_only=True)
# print(a)
sectors  = ft.groupby('Sector')
print(sectors.size())
print(sectors.groups)
print(sectors.first())
print(sectors.last())
print(sectors.nth(0))
print(sectors.get_group('Apparel'))
print(sectors.sum(numeric_only=True))
print(sectors.get_group('Energy').sum(numeric_only=True))
print(sectors.get_group('Energy').min(numeric_only=True))
print(sectors.get_group('Energy').max(numeric_only=True))
print(sectors.get_group('Energy').mean(numeric_only=True))
print(sectors.max(numeric_only=True))
print(sectors['Profits'].max(numeric_only=True))
print(sectors.agg({'Revenues':'sum','Profits':'mean','Employees':'min'}))
print(ft.nlargest(n=5,columns='Profits'))
sectors = ft.groupby(by=['Sector','Industry'])
print(sectors.get_group(('Wholesalers','Wholesalers: Health Care')))

