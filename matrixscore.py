import tbapy
import numpy as np

tba = tbapy.TBA('frc4924:test:v1.5')

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
        for p in i['alliances']['red']['teams']:
            if r['key'] == p:
                teamspermatch.append(1)
                break
        else:
            teamspermatch.append(0)

    teamstotal.append(teamspermatch)
    score = 0
#    if i['score_breakdown']['red']['rotor2Engaged'] : score += 3
#    if i['score_breakdown']['red']['rotor3Engaged'] : score += 4
#    if i['score_breakdown']['red']['rotor4Engaged'] : score += 7
    score = i['score_breakdown']['red']['totalPoints']

    rotorspermatch.append([score])
    teamspermatch = []

    for b in teams:
        for p in i['alliances']['blue']['teams']:
            if b['key'] == p:
                teamspermatch.append(1)
                break
        else:
            teamspermatch.append(0)
    teamstotal.append(teamspermatch)
    teamspermatch = []

    score = 0
#    if i['score_breakdown']['blue']['rotor2Engaged'] : score += 3
#    if i['score_breakdown']['blue']['rotor3Engaged'] : score += 4
#    if i['score_breakdown']['blue']['rotor4Engaged'] : score += 7
    score = i['score_breakdown']['blue']['totalPoints']


    rotorspermatch.append([score])

right = np.matrix(rotorspermatch)
left = np.matrix(teamstotal)
print(left.shape)
print(right.shape)
x,resid,rank,s = np.linalg.lstsq(left,right)
num = 0
opr = {}
while num < len(teams):
    #print(teams[num]["team_number"])
    #print(x[num])
    opr[teams[num]["team_number"]] = x[num]
    print(opr)
    num += 1

winnings = 0

for i in finished:
    redscore = opr[int(i['alliances']['red']['teams'][0][3:])]+opr[int(i['alliances']['red']['teams'][1][3:])]+opr[int(i['alliances']['red']['teams'][2][3:])]
    bluescore = opr[int(i['alliances']['blue']['teams'][0][3:])]+opr[int(i['alliances']['blue']['teams'][1][3:])]+opr[int(i['alliances']['blue']['teams'][2][3:])]
    print(redscore)
    print(bluescore)
    uguess = i['score_breakdown']['blue']['totalPoints'] < i['score_breakdown']['red']['totalPoints']
    rguess = bluescore < redscore
    if rguess == uguess:
        winnings += 1
        print ("right!")
    else:
        print("wrong!")
    num += 1
    print(num)
print(winnings/len(event))
