#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


q_df = pd.DataFrame([['male','teacher'],['male','engineer'],['female',None],['female','engineer']], columns=['Sex', 'Profession'])
q_df


# In[3]:


q_df.fillna("others")


# In[6]:


pf = pd.get_dummies(q_df[['Profession']])
q_df = pd.concat([q_df, pf], axis=1)
q_df


# In[ ]:




