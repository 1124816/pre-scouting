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

teams = tba.event_teams("2017flwp")
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
print(teams)
team_info = []
for i in teams.key:
    team_info.append(tba.team(i).json)
alldata = pd.DataFrame(team_info)
print(alldata)
pickle.dump( alldata, open( "save.p", "wb" ) )
