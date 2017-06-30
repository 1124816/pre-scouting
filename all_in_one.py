 #age/number in list <
 #opr/mine in event
 #dpr in event
 #ccwm in event
 #avg. gear event? mine
 #num of comps in team
 #avg rank in other comps in team in event
 #avg auto mine

import numpy as np
import pandas as pd
import tbapy
import pickle

tba = tbapy.TBA('w4sdTrGh4f4ueC0pfm5ZceCZp3yM3I0SRsJLrn1oblRowvr3Zx2UbcXQpaWnZSpK')

teams = tba.event_teams(event_code)
i = 0
while i < len(teams):
    teams[i] = teams[i].json
    i+=1

teams = pd.DataFrame(teams)
teams = teams.drop('state_prov', axis=1)
teams = teams.drop('website', axis=1)
teams = teams.drop('name', axis=1)
teams = teams.drop('motto', axis=1)
teams = teams.drop('nickname', axis=1)
teams = teams.drop('postal_code', axis=1)
teams = teams.drop('location_name', axis=1)
teams = teams.drop('lng', axis=1)
teams = teams.drop('home_championship', axis=1)
teams = teams.drop('lat', axis=1)
teams = teams.drop('gmaps_url', axis=1)
teams = teams.drop('gmaps_place_id', axis=1)
teams = teams.drop('country', axis=1)
teams = teams.drop('city', axis=1)
teams = teams.drop('address', axis=1)
#print(teams)
team_info = []
for i in teams.key:
    team_info.append(tba.team(i).json)
alldata = pd.DataFrame(team_info)
data = alldata

data = data.drop('website', axis=1)
data = data.drop('state_prov', axis=1)
data = data.drop('postal_code', axis=1)
data = data.drop('nickname', axis=1)
data = data.drop('name', axis=1)
data = data.drop('motto', axis=1)
data = data.drop('location_name', axis=1)
data = data.drop('lng', axis=1)
data = data.drop('lat', axis=1)
data = data.drop('home_championship', axis=1)
data = data.drop('gmaps_url', axis=1)
data = data.drop('gmaps_place_id', axis=1)
data = data.drop('country', axis=1)
data = data.drop('city', axis=1)
data = data.drop('address', axis=1)

data = data.set_index('key')

opr = tba.event_oprs(event_code)
opr = opr.json
opr = pd.DataFrame(opr)


data = data.join(opr)

finals = tba.event_alliances(event_code)
final_picks = []
for i in finals:
    final_picks.append(i.picks)
final_picks = [item for sublist in final_picks for item in sublist]

data['final'] = data.index.isin(final_picks)

#print(data[data['final']==True].count())

data = pickle.load( open( "final.p", "rb" ) )

team_events = []

for i in data.index:
    events = []
    tb_events = tba.team_events(i)
    for e in tb_events:
        events.append(e.json)
    team_events.append(events)

yearly_events = []
for i in team_events:
    events = []
    for p in i:
        if p['year'] == 2017 and (p['event_type'] == 0 or p['event_type'] == 1):
            events.append(p)
    yearly_events.append(events)
team_events = yearly_events

count = []
for i in team_events:
    count.append(len(i))

data['num_comps'] = count

#print(data)

data['rookie_year'] = 2017 - data['rookie_year']
