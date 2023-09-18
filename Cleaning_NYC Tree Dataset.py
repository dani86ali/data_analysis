#!/usr/bin/env python
# coding: utf-8

# In[66]:


import pandas as pd

pd.set_option('display.max_columns', None)


# In[67]:


tree_census = pd.read_csv(r'C:\Users\dani8\Downloads\2015_Street_Tree_Census_-_Tree_Data.csv')
tree_census


# In[68]:


tree_census.columns


# In[69]:


# Creating a subset of dataset by selecting columns necessary for analysis. 

tree_census_subset = tree_census[['tree_id', 'tree_dbh', 'stump_diam',
       'curb_loc', 'status', 'health', 'spc_latin', 'steward',
       'sidewalk', 'problems', 'root_stone', 'root_grate', 'root_other', 
       'trunk_wire', 'trnk_light', 'trnk_other',
       'brch_light', 'brch_shoe', 'brch_other']]

tree_census_subset
     


# In[70]:


tree_census_subset.isna().sum()


# In[71]:


tree_census_subset[tree_census_subset['health'].isna()]


# In[72]:


tree_census_subset.describe()


# In[73]:


tree_census_subset.dtypes


# In[74]:


big_trees = tree_census_subset.hist(bins=60, figsize=(20,10))


# In[75]:


big_trees=tree_census_subset[tree_census_subset['tree_dbh']>50]
big_trees


# In[76]:


big_trees[['tree_id','tree_dbh']].plot(kind='scatter', x='tree_id', y='tree_dbh', figsize=(20,10))


# In[77]:


(tree_census_subset['spc_latin'].value_counts())


# In[78]:


pd.DataFrame(tree_census_subset['spc_latin'].value_counts()).plot(kind='bar',figsize=(20,10))


# In[79]:


tree_census_subset['steward'].value_counts()


# In[80]:


tree_census_subset['sidewalk'].value_counts()


# In[32]:


tree_census_subset['curb_loc'].value_counts()


# In[81]:


Stumps = tree_census_subset [tree_census_subset['status']=='Stump']
Stumps


# In[82]:


Dead = tree_census_subset [tree_census_subset['status']=='Stump']
Dead


# In[ ]:


# Dead = tree_census_subset [tree_census_subset['status']!='Dead']
# Stumps = tree_census_subset [tree_census_subset['status']!='Stump']


# In[83]:


tree_census_subset ['health'].value_counts()


# In[84]:


tree_problems = tree_census_subset [['root_stone',
       'root_grate', 'root_other', 'trunk_wire', 'trnk_light', 'trnk_other',
       'brch_light', 'brch_shoe', 'brch_other']]

tree_problems


# In[45]:


tree_problems.apply(pd.Series.value_counts)


# In[85]:


mask = ((tree_census_subset ['status'] == 'Stump') |  (tree_census_subset ['status'] == 'Dead'))


# In[86]:


tree_census_subset.loc[mask, 'health'] = tree_census_subset.loc[mask, 'health'].fillna ('Not Applicable')


# In[87]:


tree_census_subset[tree_census_subset ['status'] == 'Stump']


# In[88]:


tree_census_subset.loc[mask] = tree_census_subset.loc[mask].fillna ('Not Applicable')


# In[89]:


tree_census_subset[tree_census_subset ['status'] == 'Stump']


# In[90]:


tree_census_subset.isna().sum()


# In[91]:


tree_census_subset [tree_census_subset['health'].isna()]


# In[92]:


tree_census_subset['steward'].value_counts()


# In[93]:


tree_census_subset [tree_census_subset['sidewalk'].isna()]


# In[94]:


tree_census_subset['sidewalk'].value_counts()


# In[95]:


tree_census_subset [tree_census_subset['spc_latin'].isna()]


# In[96]:


tree_census_subset [tree_census_subset['problems'].isna()]


# In[97]:


tree_census_subset['problems'].value_counts()


# In[98]:


tree_census_subset['problems'].fillna('None', inplace=True)
tree_census_subset['health'].fillna('Good', inplace=True)
tree_census_subset['spc_latin'].fillna('No observation', inplace=True)
tree_census_subset['sidewalk'].fillna('NoDamage', inplace=True)


# In[99]:


tree_census_subset.isna().sum()


# In[100]:


big_trees = tree_census_subset[(tree_census_subset['tree_dbh']>60) | (tree_census_subset['stump_diam']>60)]
big_trees


# In[101]:


# remove bad data from main working dataset. 

tree_census_subset = tree_census_subset[(tree_census_subset['tree_dbh']<=60) | (tree_census_subset['stump_diam']<=60)]
tree_census_subset


# In[102]:


# Separate dataset for Alive, Stump, and Dead trees

tree_census_subset_alive = tree_census_subset [tree_census_subset['status'] == 'Alive']
tree_census_subset_dead = tree_census_subset [(tree_census_subset['status'] == 'Dead') | (tree_census_subset['status'] == 'Stump')]


# In[103]:


tree_census_subset_alive.groupby('spc_latin').mean()


# In[104]:


tree_census_subset_alive.groupby('spc_latin')['tree_dbh'].describe()


# In[105]:


tree_census_subset_alive[tree_census_subset['tree_dbh']==0]


# In[108]:


stats_alive = tree_census_subset_alive.groupby('spc_latin')['tree_dbh'].describe().reset_index()[['spc_latin','25%','75%']]
stats_alive


# In[113]:


# Merge to compare minimum and maximum diameter

tree_census_subset_alive=tree_census_subset_alive.merge(stats_alive, on='spc_latin', how='left')
tree_census_subset_alive


# In[115]:


mask = tree_census_subset_alive['tree_dbh']<tree_census_subset_alive['25%']
tree_census_subset_alive.loc[mask,'tree_dbh'] = tree_census_subset_alive['25%']

mask = tree_census_subset_alive['tree_dbh']>tree_census_subset_alive['75%']
tree_census_subset_alive.loc[mask,'tree_dbh'] = tree_census_subset_alive['75%']


# In[116]:


tree_census_subset_alive


# In[ ]:




