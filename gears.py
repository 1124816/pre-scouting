import tbapy
import numpy
import pandas as pd

tba = tbapy.TBA('frc4924:test:v1.4')

events = tba.event_matches('2017flwp')
event = []
for p in events:
    if p['comp_level'] == 'qm':
        event.append(p)

#print(event)
event = pd.DataFrame(event)
#print(event)
print(event[event["match_number"] < 10])
