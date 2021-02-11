#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = sns.load_dataset('titanic')


# In[2]:


df.info()


# In[19]:


sns.barplot(x='sex',y='survived',hue='class',data=df)
plt.show()


# In[22]:


g = sns.FacetGrid(df, col='survived')
g.map(plt.hist,'sex')
plt.show()


# In[34]:


df.groupby('pclass').survived.sum()

survived = df.groupby(['pclass','sex']).survived.sum()
survived.plot(kind='bar')


# In[36]:


survived_counts = pd.crosstab([df.pclass, df.sex], df.survived)
survived_counts


# In[37]:


survived_counts.plot(kind='bar', stacked=True)


# In[38]:


sns.violinplot(data=survived_counts)
plt.show()


# In[40]:


g = sns.FacetGrid(df, col='survived')
g.map(plt.hist, 'pclass')
plt.show()

h = sns.FacetGrid(df, col='survived')
h.map(plt.hist, 'sex')
plt.show()


# In[ ]:




