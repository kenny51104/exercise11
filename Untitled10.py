#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,np.nan,60])
chinese_score = np.array([65,90,82,72,66,77])


# In[19]:


english_mean = np.nanmean(english_score)
math_mean = np.nanmean(math_score)
chinese_mean = np.nanmean(chinese_score)

english_max = np.nanmax(english_score)
math_max = np.nanmax(math_score)
chinese_max = np.nanmax(chinese_score)

english_min = np.nanmin(english_score)
math_min = np.nanmin(math_score)
chinese_min = np.nanmin(chinese_score)

english_std = np.nanstd(english_score)
math_std = np.nanstd(math_score)
chinese_std = np.nanstd(chinese_score)

print("mean:", "Eng", english_mean, "Math", math_mean, "Chinese", chinese_mean)
print("max:", "Eng", english_max, "Math", math_max,  "Chinese", chinese_max)
print("min:", "Eng", english_min, "Math", math_min,  "Chinese", chinese_min)
print("std:", "Eng", english_std, "Math", math_std,  "Chinese", chinese_std)


# In[20]:


math_score[4] = 55
math_mean = np.nanmean(math_score)
math_max = np.nanmax(math_score)
math_min = np.nanmin(math_score)
math_std = np.nanstd(math_score)
print("mean", math_mean, "max", math_max, "min", math_min, "std", math_std)


# In[14]:


a = np.corrcoef(chinese_score, math_score)
b = np.corrcoef(chinese_score, english_score)



# In[9]:


a


# In[10]:


b


# In[21]:


print("English")


# In[ ]:




