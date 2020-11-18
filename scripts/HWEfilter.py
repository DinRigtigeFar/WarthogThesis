#!/usr/bin/env python
# coding: utf-8

# ## Plot HWE filters

# In[33]:


from numpy import load
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


# In[2]:


cov2 = load("subsample_wart_minInd18_37inds_cov2.inbreed.sites.npy")
cov3 = load("subsample_wart_minInd18_37inds_cov3.inbreed.sites.npy")


# In[57]:


plt.hist(cov2, bins=22, color="green", ec="black")
plt.hist(cov3, bins=22, color="white", ec="red", alpha=0.6)
plt.title("$F_{ST}$ per site before and after HWE filtering")
plt.ylabel("Frequency")
plt.xlabel("$F_{ST}$")
cov2_plot = mpatches.Patch(color='green', label='Before filtering', ec="black")
cov3_plot = mpatches.Patch(color='white', label="After filtering", ec="red")
plt.legend(handles=[cov2_plot, cov3_plot])
plt.savefig("downsample_inbreed_site.pdf", bbox_inches = 'tight', pad_inches = 0.1)

