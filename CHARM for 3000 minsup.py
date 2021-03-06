#!/usr/bin/env python
# coding: utf-8

# In[40]:


import sys
import pandas as pd


# In[53]:


def create_dict_from_file(filename):
        f = open("mushroom.txt", "r") # file was placed in Jupyter Notebook
        d = {}
        for tids, line_items in enumerate(f):
            d[tids] = [j for j in line_items.split(' ')
                           if j != '\n']
        return d


# In[56]:


# create database
def create_database(itemset):
    "Uses dummy indexing to create the binary database"
    return pd.Series(itemset).str.join('|').str.get_dummies()

# calculate the support
def compute_support(df, column):
    "Exploits the binary nature of the database"
    return df[column].sum()

# Sys args did not work for me, used workaround to run 3000
if __name__ == '__main__':
    minsup = 3000
    filename = 'mushroom.txt'
    dict_itemset = create_dict_from_file(filename)
    database = create_database(dict_itemset)


# In[57]:


# Executes the brute force algorithm
freq_items = []
for col in database.columns:
    sup = compute_support(database, col)
    if sup >= minsup:
        freq_items.append(int(col))
    else:
        pass
print('There are %d items with frequency'      ' greater than or equal to minsup.' % len(freq_items))
print(sorted(freq_items))


# In[ ]:




