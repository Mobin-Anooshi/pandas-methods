import pandas as pd
import numpy as np
"""
    Series ==> One-Dimensional
    DataFrame ==> Two Dimensional

"""
#Series

s1 = pd.Series([1,2,3],dtype=np.int8)
print(s1)
s1.index = ['R1','R2','R3']
print(s1)

s2 = pd.Series([True ,False,True])
print(s2)

s2 = pd.Series([True ,False,True],index= ['R1','R2','R3'])
print(s2)

s3 = pd.Series({'u1':'ali','u2':'amir','u3':'kevin'})
print(s3['u1'])
print(s3.index)

s4 = pd.Series([1,2,3,4])
print(s4.index) #RangeIndex(start=0, stop=4, step=1)
print(s4.size) #4
print(s4.shape) #(4,)
print(s4.is_unique) #True
print(s4.is_monotonic_increasing) # True

s5 = pd.Series(range(0,500,1))
print(s5)
print(s5.head(5))
print(s5.tail(5))

s6 = pd.Series([1,2,3,np.nan,4])
print(s6)
print(s6.size)
print(s6.count())
print(s6.sum())
print(s6.product()) # sum before
print(s6.product(skipna=False )) #nan
print(s6.cumsum())
print(s6.pct_change())
print(s6.mean())
print(s6.min())
print(s6.max())
print(s6.describe())
print(s6.sample(2)) # Random
print(s6+4) #brodcasting