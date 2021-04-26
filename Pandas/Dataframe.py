
import pandas as pd
import numpy as np

Data_frame=pd.date_range('20200301', periods=10)

print(Data_frame)



Data_frame_one = pd.DataFrame(np.random.randn(10,4),index=Data_frame)

print(Data_frame_one)