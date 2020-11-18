#!/usr/bin/env python
# coding: utf-8

# ## Import all the stuff

# In[98]:


import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


# In[2]:


desert_range = gpd.read_file(
  "desert_range/data_0.shp")
common_range = gpd.read_file("common_range/data_0.shp")
africa_shore = gpd.read_file("africa_shore/africa_final1_dd84.shp")


# ### Do the plotting

# In[146]:


fig, ax = plt.subplots(1, 1, figsize=(10,10))
africa_shore.boundary.plot(ax=ax, color="black")
desert_range.plot(ax=ax, color="red", legend=True, label="desert")
common_range.plot(ax=ax, color="orange", alpha=0.6, legend=True, label="common")
plt.axis('off')
plt.title('Ranges of common and desert warthog', size=20)
ax.set_ylim(-35, 20)
ax.set_xlim(-20, 51.5)
common = mpatches.Patch(color='orange', alpha=0.6, label='Common warthog')
desert = mpatches.Patch(color='red', label='Desert warthog')
plt.legend(handles=[common, desert], loc="center left", prop={'size': 16})
plt.savefig("ranges.pdf", bbox_inches = 'tight', pad_inches = 0.1)

