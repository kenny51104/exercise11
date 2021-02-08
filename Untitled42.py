#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import seaborn as sns

sns.set_style('whitegrid')

rs = np.random.RandomState(7)
x = rs.normal(2, 1, 75)
y = 2+ 1.5*x + rs.normal(0, 2, 75)


sns.residplot(x, y, lowess=True, color="g")


# In[3]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
sns.set(color_codes=True)

sns.distplot(x, bins=15, kde=False, rug=True)


# In[ ]:




