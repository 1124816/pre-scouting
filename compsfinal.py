import pickle
import numpy as np
import pandas as pd
import tbapy

 #age/number in list <
 #oprin event <
 #my opr
 #dpr in event <
 #ccwm in event <
 #avg. gear event? mine
 #num of comps prev in team
 #avg rank in other comps in team in event
 #avg auto mine

tba = tbapy.TBA('w4sdTrGh4f4ueC0pfm5ZceCZp3yM3I0SRsJLrn1oblRowvr3Zx2UbcXQpaWnZSpK')


data = pickle.load( open( "opr.p", "rb" ) )
#data = data.drop('website', axis=1)
#data = data.drop('state_prov', axis=1)
#data = data.drop('postal_code', axis=1)
#data = data.drop('nickname', axis=1)
#data = data.drop('name', axis=1)
#data = data.drop('motto', axis=1)
#data = data.drop('location_name', axis=1)
#data = data.drop('lng', axis=1)
#data = data.drop('lat', axis=1)
#data = data.drop('home_championship', axis=1)
#data = data.drop('gmaps_url', axis=1)
#data = data.drop('gmaps_place_id', axis=1)
#data = data.drop('country', axis=1)
#data = data.drop('city', axis=1)
#data = data.drop('address', axis=1)

finals = tba.event_alliances("2017flwp")
final_picks = []
for i in finals:
    final_picks.append(i.picks)
final_picks = [item for sublist in final_picks for item in sublist]

data['final'] = data.index.isin(final_picks)

print(data[data['final']==True].count())


pickle.dump( data, open( "final.p", "wb" ) )
