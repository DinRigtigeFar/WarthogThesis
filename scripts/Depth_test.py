#!/usr/bin/env python
# coding: utf-8

# Do the imports and read the dataset.

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


data = pd.read_table("Warthog_GL2_trimmedGhana.depthSample", names=range(102))
new_data = pd.read_table("wart_minInd18_37inds.depthSample", names=range(102))


# New data is going to be called: wart_minInd18_37inds.depthSample

# Read in depth data with names corresponding to the depths.

# In[2]:


data


# In[3]:


new_data


# Check the amount of snp sites per individual are the same.

# In[4]:


data.sum(axis=1)


# Calculating the weighted average using numpy to see what the average depth is per individual.

# In[5]:


depth = [np.round(np.average(range(1,101), weights=data.iloc[i,1:101]), 2) for i in range(len(data))]
print(depth)
print(min(depth), max(depth))
low_depth = [i for i in depth if i<10]
print(low_depth)
print(min(low_depth), max(low_depth))
hi_depth = [i for i in depth if i>10]
print(hi_depth)
print(min(hi_depth), max(hi_depth))


# In[6]:


new_depth = [np.round(np.average(range(1,101), weights=new_data.iloc[i,1:101]), 2) for i in range(len(new_data))]
print(new_depth)
print(min(new_depth), max(new_depth))
new_low_depth = [i for i in new_depth if i<10]
print(new_low_depth)
print(min(new_low_depth), max(new_low_depth))
new_hi_depth = [i for i in new_depth if i>10]
print(new_hi_depth)
print(len(new_hi_depth))
print(min(new_hi_depth), max(new_hi_depth))


# Plot the average depths on an individual basis.

# In[7]:


plt.scatter(range(len(low_depth)), low_depth)
plt.ylabel("Average depth per individuals")
plt.xlabel("Individual number")
plt.title("Depths of 'low depth' individuals")
plt.ylim(3,7)
plt.text(10, 4.6, f'Average depth \n= {np.round(np.mean(low_depth),2)}')
plt.hlines(np.mean(low_depth), xmin=0, xmax=33, linestyles="dashed")
#plt.savefig('low_depth.pdf')
plt.show()

plt.scatter(range(len(hi_depth)), hi_depth)
plt.ylabel("Average depth per individuals")
plt.xlabel("Individual number")
plt.title("Depths of 'high depth' individuals")
plt.ylim(16,18)
plt.text(2, 17, f'Average depth \n= {np.round(np.mean(hi_depth),2)}')
plt.hlines(np.mean(hi_depth), xmin=0, xmax=len(hi_depth), linestyles="dashed")
#plt.savefig('high_depth.pdf')
plt.show()


# In[8]:


plt.scatter(range(len(new_low_depth)), new_low_depth)
plt.ylabel("Average depth per individual")
plt.xlabel("Individual number")
plt.title("Depths of 'low depth' individuals")
plt.ylim(3,7)
plt.text(10, 4.6, f'Average depth \n= {np.round(np.mean(new_low_depth),2)}')
plt.hlines(np.mean(new_low_depth), xmin=0, xmax=33, linestyles="dashed")
#plt.savefig('new_low_depth.pdf')
plt.show()


plt.scatter(range(len(new_hi_depth)), new_hi_depth)
plt.ylabel("Average depth per individual")
plt.xlabel("Individual number")
plt.title("Depths of 'high depth' individuals")
plt.ylim(16,18.5)
plt.text(2, 17, f'Average depth \n= {np.round(np.mean(new_hi_depth),2)}')
plt.hlines(np.mean(new_hi_depth), xmin=0, xmax=len(new_hi_depth), linestyles="dashed")
#plt.savefig('new_high_depth.pdf')
plt.show()


# In[5]:


new2020_data = pd.read_table("47indsForPCA.depthSample", names=range(102))
new2020_data


# In[6]:


new2020_depth = [np.round(np.average(range(1,101), weights=new2020_data.iloc[i,1:101]), 2) for i in range(len(new2020_data))]
print(new2020_depth)
print(min(new2020_depth), max(new2020_depth))
new2020_low_depth = [i for i in new2020_depth if i<10]
print(new2020_low_depth)
print(min(new2020_low_depth), max(new2020_low_depth))
new2020_hi_depth = [i for i in new2020_depth if i>10]
print(new2020_hi_depth)
print(len(new2020_hi_depth))
print(min(new2020_hi_depth), max(new2020_hi_depth))


# In[14]:


plt.scatter(range(len(new2020_low_depth)), new2020_low_depth)
plt.ylabel("Average depth per individual")
plt.xlabel("Individual number")
plt.title("Depths of 'low depth' individuals")
#plt.ylim(3,7)
plt.text(10, 6, f'Average depth \n= {np.round(np.mean(new2020_low_depth),2)}')
plt.hlines(np.mean(new2020_low_depth), xmin=0, xmax=33, linestyles="dashed")
plt.savefig('new2020_low_depth.pdf')
plt.show()


plt.scatter(range(len(new2020_hi_depth)), new2020_hi_depth)
plt.ylabel("Average depth per individual")
plt.xlabel("Individual number")
plt.title("Depths of 'high depth' individuals")
#plt.ylim(16,18.5)
plt.text(5, 20, f'Average depth \n= {np.round(np.mean(new2020_hi_depth),2)}')
plt.hlines(np.mean(new2020_hi_depth), xmin=0, xmax=len(new2020_hi_depth), linestyles="dashed")
plt.savefig('new2020_high_depth.pdf')
plt.show()

