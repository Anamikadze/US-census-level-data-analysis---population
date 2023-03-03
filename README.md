## Joining Geographic and Census Data

## Input Data

The first input file is **county_geo.csv**. It has five fields: `"STATEFP"`, `"COUNTYFP"`, `"GEOID"`, `"ALAND"`, and `"AWATER"`. The first two, `"STATEFP"` and `"COUNTYFP"`, are the state FIPS code (2 digits) and the county FIPS code within the state (3 digits). The third, `"GEOID"`, is a 5-digit FIPS code that uniquely identifies the county within the US. It consists the state and county codes concatenated together. The last two variables are the areas of land and water in the county in square meters.

The second input file is **county_pop.csv**. It has four fields: `"NAME"`, `"B01001_001E"`, `"state"`, `"county"`. The first is the name of the county, including its state. The second, `"B01001_001E"`, is the Census variable giving the total population of the county. The third and fourth fields give the FIPS codes for the state and the county within the state (the same information as `"STATEFP"` and `"COUNTYFP"` in the other file).

## Deliverables

There is one deliverable: a script called **county_merge.py** that joins the population data onto the geographic data, calculates several variables, including each county's percentage of its state's total population, writes out the result as a new CSV file, and draws four graphs. 


