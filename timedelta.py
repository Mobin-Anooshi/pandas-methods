import pandas as pd
import datetime as dt
from pandas.tseries.offsets import DateOffset

print(pd.Timestamp(year=1991,month=4,day=12))
print(pd.Timestamp(year=1991,month=4,day=12) == dt.datetime(year=1991,month=4,day=12))
print(pd.Timestamp(ts_input='1991-04-12'))
print(pd.Timestamp(ts_input='1991/04/12'))
print(pd.Timestamp(ts_input='1991/04/12 8:50:2 PM'))
print(pd.Timestamp(ts_input=dt.datetime(2020,4,12,12,32,43,330000,)))
timestamps =  [
    pd.Timestamp('2000-01-01'),
    pd.Timestamp('2000-01-02'),
    pd.Timestamp('2000-01-03')
]
a1 = pd.Series(['amir','kevin','jack'],index=timestamps)
print(a1)
morning = pd.Timestamp('2020-01-01 2:30:20 AM')
evening = pd.Timestamp('2020-01-01 2:30:20 PM')
print(morning < evening)

disney = pd.read_csv('csvs/disney.csv')
disney['Date'] = pd.to_datetime(disney['Date'])
print(disney['Date'].dt.year)
print(disney['Date'].dt.dayofweek)
print(disney['Date'].dt.month_name())
disney['Week_day'] = disney['Date'].dt.day_name()
g = disney.groupby('Week_day')
print(g.mean(numeric_only=True))

disney = pd.read_csv('csvs/disney.csv',parse_dates=['Date'])
print(disney['Date']+DateOffset(days=2))

print(pd.to_timedelta('3 hour, 5 minutes, 12 seconds'))
print(pd.Timestamp('1991-5-5')-pd.Timestamp('1990-5-5'))

dlv = pd.read_csv('csvs/deliveries.csv',parse_dates=['order_date','delivery_date'])
dlv['duration'] = dlv['delivery_date']-dlv['order_date']
print(dlv)
print(dlv.sort_values('duration'))