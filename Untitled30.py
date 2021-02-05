#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[26]:


score_df = pd.DataFrame([[1,56,66,70], [2,90,45,34], [3,45,32,55], [4,70,77,89], [5,56,80,70], [6,60,54,55], [7,45,70,79], [8,34,77,76], [9,25,87,60], [10,88,40,43]],columns=['student_id','math_score','english_score','chinese_score'])
score_df = score_df.set_index('student_id')
score_df


# In[18]:


score_df.loc[6].mean()


# In[20]:


score_df.mean(axis=1).median()


# In[21]:


print("沒有")


# In[22]:


score_df.apply(lambda x : x**(0.5)*10).loc[6]


# In[24]:


score_df.apply(lambda x : x**(0.5)*10).mean()


# In[ ]:





# In[ ]:




