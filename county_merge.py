#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 17:48:16 2023

@author: anano
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.dpi"] = 300 #setting resolution to 300

#%%
fips_list = ["STATEFP", "COUNTYFP", "GEOID", "state", "county"] #creates a list containing five elements
fips_cols = {col:str for col in fips_list} #uses ductionary comprehension that sets elements of fips_list as keys
# and str as each entry's value
geo_data = pd.read_csv("county_geo.csv", dtype=fips_cols) # reads in the "gounty_geo.csv" file and stores it 
#in a Pandas DataFrame called geo_data; indicates that it contains FIPS codes
pop_data = pd.read_csv("county_pop.csv",dtype=fips_cols ) 

#%%
geo_states = set(geo_data["STATEFP"]) #contains unique values of the "STATEFP" column from the geo_data dataframe
pop_states = set(pop_data["state"])
print("Set of differences Bbtween geo_data and pop_data: ", geo_states - pop_states) #The set difference geo_states - 
#pop_states returns all the entries in geo_states that are not in pop_states. NOW ITS EMPTY - there are no differences
print("Set difference between pop_states and geo_states: ", pop_states - geo_states) # include any states that are
# in pop_states but not in geo_states, which is expected to include Puerto Rico, since it is not included in this particular geography file.

#%%
merged = geo_data.merge(pop_data, left_on=["STATEFP","COUNTYFP"], right_on=["state","county"], how="left")
#merges geo_data(left) to pop_data(right), merged on matching columns ["STATEFP","COUNTYFP"] in the left dataframe (geo_data) 
#and ["state","county"] in the right dataframe (pop_data)
merged = merged.set_index(["STATEFP","COUNTYFP"]) #sets index to selected columns
merged = merged.rename(columns={"B01001_001E": "pop"}) #changes the column name "B01001_001E" to "pop" in the merged dataframe
merged["sq_km"] = (merged["ALAND"])/1e6 #displayes area in millions of km
merged["density"] = (merged["pop"])/(merged["sq_km"]) #displays population density
merged["pop_mil"] = (merged["pop"])/1e6
group_by_state = merged.groupby("STATEFP") #groups by Statefp
state_pop = group_by_state["pop"].sum()
merged["percent"] = (merged["pop"]/state_pop)*100 # displays's each county's population of percent share in relevant state
merged=merged.sort_index()
merged.to_csv("county_merge.csv") #creates new csv file to store merged dataframe

#%%
plot_info = [("sq_km", "Square km", "area"), ("pop_mil", "Millions of people", "population"), ("density", "People per square km", "density"), ("percent", "Percent", "share of state population")]
nfig = 1
for var, units, ftitle in plot_info:
    sort_by_var = merged.sort_values(var)
    last10 = sort_by_var[-10:] #Selects the last 10 rows (highest values)
    fig,ax = plt.subplots() # Creates a new figure and axes
    fig.suptitle(f"Figure {nfig}: Top 10 counties for {ftitle}") #sets overall title
    last10.plot.barh(x="NAME", y=var, ax=ax, legend=None)
    ax.set_ylabel(None) #turns of y axis
    ax.set_xlabel(units) # Sets x-axis label to appropriate units
    ax.set_xlabel(units)
    plt.tight_layout()
    fig.savefig(f"fig{nfig}_{var}.png")
    nfig += 1
 

