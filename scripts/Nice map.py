#!/usr/bin/env python
# coding: utf-8

# # Make a nice map, including ranges, of the samples

# In[1]:


import matplotlib.pyplot as plt 
import numpy as np
import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt
import io
from urllib.request import urlopen, Request
from PIL import Image
import pandas as pd
import seaborn as sns
import geopandas as gpd
import matplotlib.patches as mpatches


# In[2]:


df = pd.read_csv('39inds_locations_sorted.txt', sep='\t')


# In[3]:


def image_spoof(self, tile): # this function pretends not to be a Python script
    url = self._image_url(tile) # get the url of the street map API
    req = Request(url) # start request
    req.add_header('User-agent','Anaconda 3') # add user agent to request
    fh = urlopen(req) 
    im_data = io.BytesIO(fh.read()) # get image
    fh.close() # close url
    img = Image.open(im_data) # open image with PIL
    img = img.convert(self.desired_tile_form) # set image format
    return img, self.tileextent(tile), 'lower' # reformat for cartopy

cimgt.Stamen.get_image = image_spoof # reformat web request for street map spoofing
osm_img = cimgt.Stamen('terrain-background') # spoofed, downloaded street map


# In[9]:


fig = plt.figure(figsize=(12,9)) # open matplotlib figure
ax1 = plt.axes(projection=osm_img.crs) # project using coordinate reference system (CRS) of street map
center_pt = [-5.914655, 20.185829] # lat/lon of One World Trade Center in NYC
zoom = 22 # for zooming out of center point
extent = [center_pt[1]-(zoom*1.8),center_pt[1]+(zoom*1.5),center_pt[0]-(zoom*1.05),center_pt[0]+zoom] # adjust to zoom
ax1.set_extent(extent) # set extents

scale = np.ceil(-np.sqrt(2)*np.log(np.divide(zoom,350.0))) # empirical solve for scale based on zoom
scale = (scale<20) and scale or 19 # scale cannot be larger than 19
ax1.add_image(osm_img, int(scale)) # add OSM with zoom specification
# NOTE: zoom specifications should be selected based on extent:
# -- 2     = coarse image, select for worldwide or continental scales
# -- 4-6   = medium coarseness, select for countries and larger states
# -- 6-10  = medium fineness, select for smaller states, regions, and cities
# -- 10-12 = fine image, select for city boundaries and zip codes
# -- 14+   = extremely fine image, select for roads, blocks, buildings
plt.title('Proposed expansion of the common warthog', fontsize=20)
desert_range.plot(ax=ax1, color="red", alpha=0.7, legend=True, label="desert")
common_range.plot(ax=ax1, color="orange", alpha=0.3, legend=True, label="common")
g = sns.scatterplot(x="Latitude", y="Longitude", hue="Species and Country", data=df, transform=ccrs.Geodetic(), palette=["#A65628", "#E41A1C", "#377EB8", "#984EA3", "#4DAF4A", "#FF7F00", "#F0C000"], s=250)
common = mpatches.Patch(color='orange', alpha=0.3, label='$\it{P. africanus}$ range')
desert = mpatches.Patch(color='red', alpha=0.7, label="$\it{P. aethiopicus}$ range")
forest = mpatches.Patch(color='#82a262', label='Dense forest')
handles, labels = ax1.get_legend_handles_labels()
plt.legend(handles=handles[1:]+[common, desert, forest],loc='lower left', prop={'size': 15}, markerscale=3)
#plt.savefig('forDisc_Nice_map.pdf', bbox_inches = 'tight', pad_inches = 0.0) # save the plot with good borders
plt.show() # show the plot


# ## Overall map (55 individuals total)

# In[6]:


all_coords_raw = """Ghana n=16,9.5,-2.0
Kenya n=10,-1.3,36.8
Tanzania n=13,-5.8,31.1
Zambia n=1,-15.4,28.3
Zimbabwe n=8,-19.8,29.4
Namibia n=7,-23.0,18.5"""

all_coords = [i.split(",") for i in all_coords_raw.split("\n")]
all_df = pd.DataFrame()
all_df["Countries"] = [i[0] for i in all_coords]
all_df["Lats"] = [float(i[1]) for i in all_coords]
all_df["Longs"] = [float(i[2]) for i in all_coords]


# ## Include ranges

# In[5]:


desert_range = gpd.read_file("../ranges_maps/desert_range/data_0.shp")
common_range = gpd.read_file("../ranges_maps/common_range/data_0.shp")
common_range = common_range.to_crs("EPSG:3395")
desert_range = desert_range.to_crs("EPSG:3395")


# ## Make map of all samples including ranges

# In[44]:


fig = plt.figure(figsize=(12,9)) # open matplotlib figure
ax1 = plt.axes(projection=osm_img.crs) # project using coordinate reference system (CRS) of street map
center_pt = [-5.914655, 20.185829] # lat/lon of One World Trade Center in NYC
zoom = 22 # for zooming out of center point
extent = [center_pt[1]-(zoom*1.8),center_pt[1]+(zoom*1.5),center_pt[0]-(zoom*1.05),center_pt[0]+zoom] # adjust to zoom
ax1.set_extent(extent) # set extents

scale = np.ceil(-np.sqrt(2)*np.log(np.divide(zoom,350.0))) # empirical solve for scale based on zoom
scale = (scale<20) and scale or 19 # scale cannot be larger than 19
ax1.add_image(osm_img, int(scale)) # add OSM with zoom specification
# NOTE: zoom specifications should be selected based on extent:
# -- 2     = coarse image, select for worldwide or continental scales
# -- 4-6   = medium coarseness, select for countries and larger states
# -- 6-10  = medium fineness, select for smaller states, regions, and cities
# -- 10-12 = fine image, select for city boundaries and zip codes
# -- 14+   = extremely fine image, select for roads, blocks, buildings
plt.title('Sample countries for 55 sequenced warthogs', fontsize=20)
desert_range.plot(ax=ax1, color="red", alpha=0.7, legend=True, label="desert")
common_range.plot(ax=ax1, color="orange", alpha=0.3, legend=True, label="common")
g = sns.scatterplot(x="Longs", y="Lats", hue="Countries", data=all_df, transform=ccrs.Geodetic(), palette=["#E41A1C", "#377EB8", "#984EA3", "#4DAF4A", "#FF7F00", "#F0C000"], s=250)

common = mpatches.Patch(color='orange', alpha=0.3, label='$\it{P. africanus}$ range')
desert = mpatches.Patch(color='red', alpha=0.7, label="$\it{P. aethiopicus}$ range")
forest = mpatches.Patch(color='#82a262', label='Dense forest')
handles, labels = ax1.get_legend_handles_labels()
plt.legend(handles=handles[1:]+[common, desert, forest],loc='lower left', prop={'size': 15}, markerscale=3)
#plt.savefig('55_warts_map.pdf', bbox_inches = 'tight', pad_inches = 0.0) # save the plot
plt.show() # show the plot

