#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


score_df = pd.DataFrame([[1,50,80,70,'boy',1],[2,60,45,50,'boy',2],[3,98,43,55,'boy',1],[4,70,69,89,'boy',2],[5,56,79,60,'girl',1],[6,60,68,55,'girl',2],[7,45,70,77,'girl',1],[8,55,77,76,'girl',2],[9,25,57,60,'girl',1],[10,88,40,43,'girl',3],[11,25,60,45,'boy',3],[12,80,60,23,'boy',3],[13,20,90,66,'girl',3],[14,50,50,50,'girl',3],[15,89,67,77,'girl',3]],columns=['student_id','math_score','english_score','chinese_score','sex','class'])
score_df


# In[37]:


score_df.groupby(['class']).agg(['max','min'])


# In[16]:


#math_score 98 20
#english_score 90 40
#chinese_score 89 23


# In[34]:


score_df.groupby(['class'])['math_score'].mean().idxmax()


# In[ ]:


#2


# In[22]:


sex = score_df.groupby(['sex']).mean()
sex.iloc[0] - sex.iloc[1]


# In[23]:


#相差7.333333分

