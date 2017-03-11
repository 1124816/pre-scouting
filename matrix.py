import tbapy
import numpy as np
#x,resid,rank,s = np.linalg.lstsq(left,right)
#eft = np.matrix([[2, -1],[1,2],[1,1]])
tba = tbapy.TBA('frc4924:test:v1.5')

event = tba.event_matches('2017flwp')
teams = tba.event_teams('2017flwp')
opr = tba.event_stats('2017flwp')['oprs']

rotorspermatch = []
teamstotal = []
teamspermatch = []

finished = []
for i in event:
    if i['score_breakdown']:
         finished.append(i)



for i in finished:
    for r in teams:
        for p in i['alliances']['red']['teams']:
            if r['key'] == p:
                teamspermatch.append(1)
        else:
            teamspermatch.append(0)

    teamstotal.append(teamspermatch)
    score = 0
    if i['score_breakdown']['red']['rotor2Engaged'] : score += 2
    if i['score_breakdown']['red']['rotor3Engaged'] : score += 4
    if i['score_breakdown']['red']['rotor4Engaged'] : score += 6

    rotorspermatch.append([score])
    teamspermatch = []

    for b in teams:
        for p in i['alliances']['red']['teams']:
            if b['key'] == p:
                teamspermatch.append(1)
        else:
            teamspermatch.append(0)
    teamstotal.append(teamspermatch)
    teamspermatch = []

    score = 0
    if i['score_breakdown']['blue']['rotor2Engaged'] : score += 2
    if i['score_breakdown']['blue']['rotor3Engaged'] : score += 4
    if i['score_breakdown']['blue']['rotor4Engaged'] : score += 6

    rotorspermatch.append([score])

right = np.matrix(rotorspermatch)
left = np.matrix(teamstotal)
x,resid,rank,s = np.linalg.lstsq(left,right)
#print(x)

while True:
    matcha = input("lolz")
    match = tba.match('2017flwp_qm'+matcha)
    score = 0
    if match['score_breakdown']['blue']['rotor2Engaged'] : score += 2
    if match['score_breakdown']['blue']['rotor3Engaged'] : score += 4
    if match['score_breakdown']['blue']['rotor4Engaged'] : score += 6
    print(score)
    print('blue')
    bluescore = 0
    for p in match['alliances']['blue']['teams']:
        i = 0
        while i < len(teams):
            if teams[i]['key'] == p:
                bluescore += x[i][0]
                print(x[i][0])
            i += 1

    print(bluescore)
