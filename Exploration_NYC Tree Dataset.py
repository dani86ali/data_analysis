#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

pd.set_option('display.max_columns', None)


# In[3]:


tree_census = pd.read_csv(r'C:\Users\dani8\Downloads\2015_Street_Tree_Census_-_Tree_Data.csv')
tree_census


# In[4]:


tree_census.columns


# In[5]:


# Creating a subset of dataset by selecting columns necessary for analysis. 

tree_census_subset = tree_census[['tree_id', 'tree_dbh', 'stump_diam',
       'curb_loc', 'status', 'health', 'spc_latin', 'spc_common', 'steward',
       'guards', 'sidewalk', 'problems', 'root_stone',
       'root_grate', 'root_other', 'trunk_wire', 'trnk_light', 'trnk_other',
       'brch_light', 'brch_shoe', 'brch_other']]

tree_census_subset
     


# In[6]:


tree_census_subset.isna().sum()


# In[7]:


tree_census_subset[tree_census_subset['health'].isna()]


# In[8]:


tree_census_subset.describe()


# In[9]:


tree_census_subset.dtypes


# In[10]:


big_trees = tree_census_subset.hist(bins=60, figsize=(20,10))


# In[14]:


big_trees=tree_census_subset[tree_census_subset['tree_dbh']>50]
big_trees


# In[15]:


big_trees[['tree_id','tree_dbh']].plot(kind='scatter', x='tree_id', y='tree_dbh', figsize=(20,10))


# In[30]:


(tree_census_subset['spc_latin'].value_counts())


# In[28]:


pd.DataFrame(tree_census_subset['spc_latin'].value_counts()).plot(kind='bar',figsize=(20,10))


# In[29]:


tree_census_subset['steward'].value_counts()


# In[31]:


tree_census_subset['sidewalk'].value_counts()


# In[32]:


tree_census_subset['curb_loc'].value_counts()


# In[40]:


Stumps = tree_census_subset [tree_census_subset['status']=='Stump']
Stumps


# In[41]:


Dead = tree_census_subset [tree_census_subset['status']=='Stump']
Dead


# In[43]:


tree_problems = tree_census_subset [['root_stone',
       'root_grate', 'root_other', 'trunk_wire', 'trnk_light', 'trnk_other',
       'brch_light', 'brch_shoe', 'brch_other']]

tree_problems


# In[45]:


tree_problems.apply(pd.Series.value_counts)


# In[ ]:




