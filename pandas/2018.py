import pickle
import numpy as np
import pandas as pd
import tbapy
import os

tba = tbapy.TBA(os.environ['TBAKEY'])
teams = tba.event_teams('2018alhu')

data = pd.read_pickle("week3.p")

oprs = {}
for i in teams:
    if i['key'] in data.index:
        oprs[i['key']] = data.loc[i['key']]['oprs']

print(oprs)
