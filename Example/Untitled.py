#%%
import numpy as np
import pandas as pd


# In[18]
data = np.array([["uBiome", 100],
                 ["Globant", 200]])


# In[22]
df_columns = ["Company", "Total Workers"]


# In[24]
data


# In[26]
df = pd.DataFrame(data=data, columns=df_columns)


# In[28]
df


# In[31]
type(df)


# In[33]
len(df)


# In[ ]


