import pandas as pd
import numpy as np



Dict=pd.DataFrame({
    '1':[1,2,3,4,5,6,7,8,9],
    '2':pd.Timestamp('20200301')

})

print(Dict)

print(Dict.head())

print(Dict.tail())

print(Dict.index())