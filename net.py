import tbapy

tba = tbapy.TBA('frc4924:test:v1.2')

event = tba.event_matches('2017flwp')

finished = []
for i in event:
    if i['score_breakdown']:
         finished.append(i)

rotorpoints = 0


for i in finished:
    rotorpoints += i['score_breakdown']['blue']['teleopRotorPoints']
    rotorpoints += i['score_breakdown']['red']['teleopRotorPoints']

print(finished)

print("average points for rotors: ")
print(rotorpoints/(2*len(finished)))
