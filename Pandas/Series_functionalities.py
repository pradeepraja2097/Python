import pandas as pd
import numpy as np

Series_array=([1,2,3,4,5])
Index=(['A','B','C','D','E'])
Series1=pd.Series(Series_array,index=Index)
print(Series1)

Series_array1=({'A':1,'B':2})

print(pd.Series(Series_array1))