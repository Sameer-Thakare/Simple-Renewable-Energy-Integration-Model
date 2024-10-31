#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("mar_2023_energy_data.csv", index_col=1)  #reading the dataset

#importing the pypsa
import pypsa
n = pypsa.Network() #initialising an empty network.

n.add("Bus", "electricity")  #add a single bus
n.set_snapshots(data.index)   #setting the snapshots for the network

#adding all the technologies we are going to include as carriers.
carriers = [
    "thermal",
    "gas",
    "solar",
    "wind",
    "hydrogen storage underground",
    "battery storage",
]

n.add(
    "Carrier",
    carriers,
    color=["dodgerblue", "aquamarine", "gold", "indianred", "magenta", "yellowgreen"],
    co2_emissions=[0.9, 0.4, 0, 0, 0, 0],
)

# adding the demand time series to the model.
n.add(
    "Load",
    "demand",
    bus="electricity",
    p_set=data.STATE_DEMAND,
)

#adding dispatchable generation technology to the model
n.add(
    "Generator",
    "thermal",
    bus="electricity",
    carrier="thermal",
    p_nom= 16757,
    p_nom_min = 11144,
    p_nom_max = 17000,
    capital_cost=5e7,
    marginal_cost=2000,
    efficiency=0.35,
    p_nom_extendable=True,
)

n.add(
    "Generator",
    "gas",
    bus="electricity",
    carrier="gas",
    #p_nom= 10554,
    #p_nom_min = 4096,
    #p_nom_max = 10600,
    p_nom= 8554,
    capital_cost=6e7,
    marginal_cost=4000,
    efficiency=0.50,
    p_nom_extendable=True,
)

#Adding the variable renewable generators
n.add(
    "Generator",
    "wind",
    bus="electricity",
    carrier="wind",
    p_nom= 1790,
    p_nom_min = 58,
    p_nom_max = 1850,
    p_max_pu= data["WIND"]/1790,
    capital_cost=6e7,
    marginal_cost=1500,
    efficiency=0.25,
    p_nom_extendable=True,
)

n.add(
    "Generator",
    "solar",
    bus="electricity",
    carrier="solar",
    p_nom= 2305,
    p_nom_min = 10,
    p_nom_max = 2350,
    p_max_pu=data["SOLAR"]/2305,
    capital_cost=5e7,
    marginal_cost= 1000,
    efficiency=0.20,
    p_nom_extendable=True,
)

#solving the model
n.optimize(solver_name="highs")

#total system cost in million rupees per year:
print('Total System Cost in Million Rupees per Year:', n.objective / 1e6)

#The optimised capacities in MW:
print('The optimised capacities in MW:\n', n.generators.p_nom_opt)  # MW

n.statistics()

