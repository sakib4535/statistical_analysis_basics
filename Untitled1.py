#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import pickle

file_name = "load.csv"


# In[10]:


col = None
data = []
with open(file_name) as f:
    for line in f.readlines():
        vals = line.replace("\n", "").split(",")
        if col is  None:
            col = vals
        else:
            data.append([float(x) for x in vals])
            
e0 = pd.DataFrame(data, columns=col)
print(e0.dtypes)
e0.head()


# In[14]:


d0 = np.loadtxt(file_name, skiprows=1, delimiter=",")
print(d0.dtype)
print(d0[:10, :5])


# In[22]:


f0 = np.genfromtxt(file_name, delimiter=",", names=True, dtype=None)
print(f0.dtype)
print(f0[:25])


# In[24]:


h0 = pd.read_csv(file_name)
print(h0)


# In[ ]:




