import tbapy
import numpy as np
import os

tba = tbapy.TBA(os.environ['TBAKEY'])

event = tba.event_matches('2017alhu')
teams = tba.event_teams('2017alhu')

rotorspermatch = []
teamstotal = []
teamspermatch = []

finished = []
for i in event:
    if i['score_breakdown']:
         finished.append(i)



for i in finished:
    for r in teams:
        for p in i['alliances']['red']['team_keys']:
            if r['key'] == p:
                teamspermatch.append(1)
                break
        else:
            teamspermatch.append(0)

    teamstotal.append(teamspermatch)
    score = 0
    if i['score_breakdown']['red']['rotor2Engaged'] : score += 3
    if i['score_breakdown']['red']['rotor3Engaged'] : score += 4
    if i['score_breakdown']['red']['rotor4Engaged'] : score += 7

    rotorspermatch.append([score])
    teamspermatch = []

    for b in teams:
        for p in i['alliances']['blue']['team_keys']:
            if b['key'] == p:
                teamspermatch.append(1)
                break
        else:
            teamspermatch.append(0)
    teamstotal.append(teamspermatch)
    teamspermatch = []

    score = 0
    if i['score_breakdown']['blue']['rotor2Engaged'] : score += 3
    if i['score_breakdown']['blue']['rotor3Engaged'] : score += 4
    if i['score_breakdown']['blue']['rotor4Engaged'] : score += 7

    rotorspermatch.append([score])

right = np.matrix(rotorspermatch)
left = np.matrix(teamstotal)
x,resid,rank,s = np.linalg.lstsq(left,right)
num = 0
while num < len(teams):
    print(teams[num]["team_number"])
    print(x[num]+1)
    num += 1
