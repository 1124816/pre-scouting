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


data = pickle.load( open( "final.p", "rb" ) )
team_events = pickle.load( open( "teamevents.p", "rb" ) )

#team_events = []
#
#for i in data.index:
#    events = []
#    tb_events = tba.team_events(i)
#    for e in tb_events:
#        events.append(e.json)
#    team_events.append(events)

#pickle.dump( team_events, open( "teamevents.p", "wb" ) )
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

print(data)

pickle.dump( data, open( "numcomp.p", "wb" ) )
