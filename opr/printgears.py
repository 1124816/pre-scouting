import tbapy
import numpy
import pandas as pd

tba = tbapy.TBA('frc4924:test:v1.4')

events = tba.event_matches('2017alhu')
for i in events:
    print(i['score_breakdown']['blue']['rotor1Engaged'])
    print(i['score_breakdown']['blue']['rotor2Engaged'])
    print(i['score_breakdown']['blue']['rotor3Engaged'])
    print(i['score_breakdown']['blue']['rotor4Engaged'])
event = pd.DataFrame(events)
#print(event)
#print(event[event["match_number"] < 10])
