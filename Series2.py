import pandas as pd

"""
    Series methods
"""

# Series
pokemon = pd.read_csv('csvs/pokemon.csv',
                      index_col='Pokemon').squeeze()
print(pokemon)

google = pd.read_csv('csvs/google_stocks.csv',
                     parse_dates=['Date'],
                     index_col='Date').squeeze('columns')
print(google)

battle = pd.read_csv('csvs/revolutionary_war.csv',
                     parse_dates=['Start Date'],
                     index_col='Start Date',
                     usecols=['State','Start Date']).squeeze('columns')
print(battle)


print(battle.dropna().sort_values(ascending=False,na_position='last')) # sort values
print(battle.sort_index(ascending=False,na_position='last')) # sort values


print(google.nlargest()) # default 5
print(google.nsmallest()) # default 5
print(battle.value_counts(ascending=True))
print(battle.nunique())
print(battle.value_counts(normalize=True)*100)
print(google.value_counts(bins=[100,200,400,600,1000]))
print(google.value_counts(bins=6))
print(battle.index.value_counts())
print(google.apply(round)) # send to func
