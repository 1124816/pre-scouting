import tbapy
import numpy as np


tba = tbapy.TBA('frc4924:test:v1.4')

events = tba.event_matches('2017flwp')
teams = tba.event_teams('2017flwp')

event = []
for p in events:
    if p['comp_level'] == 'qm':
        event.append(p)
finished = []
winnings = 0
def score(num):
    global winnings
    finished = []
    for i in event:
        if i['match_number'] < num:
            finished.append(i)

    rotorspermatch = []
    teamstotal = []
    teamspermatch = []

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
        score = i['score_breakdown']['blue']['totalPoints']
        rotorspermatch.append([score])

    right = np.matrix(rotorspermatch)
    left = np.matrix(teamstotal)
    #print(left.shape)
    #print(right.shape)
    x,resid,rank,s = np.linalg.lstsq(left,right)
    bum = 0
    opr = {}
    while bum < len(teams):
        opr[teams[bum]["team_number"]] = x[bum]
        #print(opr)
        bum += 1

    binnings = 0

    for i in events:
        redscore = opr[int(i['alliances']['red']['teams'][0][3:])]+opr[int(i['alliances']['red']['teams'][1][3:])]+opr[int(i['alliances']['red']['teams'][2][3:])]
        bluescore = opr[int(i['alliances']['blue']['teams'][0][3:])]+opr[int(i['alliances']['blue']['teams'][1][3:])]+opr[int(i['alliances']['blue']['teams'][2][3:])]
        #print(redscore)
        #print(bluescore)
        uguess = i['score_breakdown']['blue']['totalPoints'] < i['score_breakdown']['red']['totalPoints']
        rguess = bluescore < redscore
        if rguess == uguess:
            binnings += 1
            #print ("right!")
    #    else:
            #print("wrong!")
        #num += 1
        #print(num)
    print(binnings/len(events))

    #redscore = score[event[num]['alliances']['red']['teams'][0]]['score']+score[event[num]['alliances']['red']['teams'][1]]['score']+score[event[num]['alliances']['red']['teams'][2]]['score']
    #bluescore = score[event[num]['alliances']['blue']['teams'][0]]['score']+score[event[num]['alliances']['blue']['teams'][1]]['score']+score[event[num]['alliances']['blue']['teams'][2]]['score']
    redscore = opr[int(event[num]['alliances']['red']['teams'][0][3:])]+opr[int(event[num]['alliances']['red']['teams'][1][3:])]+opr[int(event[num]['alliances']['red']['teams'][2][3:])]
    bluescore = opr[int(event[num]['alliances']['blue']['teams'][0][3:])]+opr[int(event[num]['alliances']['blue']['teams'][1][3:])]+opr[int(event[num]['alliances']['blue']['teams'][2][3:])]
    #redscore = opr[event[num]['alliances']['red']['teams'][0][3:]]+opr[event[num]['alliances']['red']['teams'][1][3:]]+opr[event[num]['alliances']['red']['teams'][2][3:]]
    #bluescore = opr[event[num]['alliances']['blue']['teams'][0][3:]]+opr[event[num]['alliances']['blue']['teams'][1][3:]]+opr[event[num]['alliances']['blue']['teams'][2][3:]]
    rguess = bluescore < redscore
    uguess = event[num]['score_breakdown']['blue']['totalPoints'] < event[num]['score_breakdown']['red']['totalPoints']
    if rguess == uguess:
        winnings += 1
        print ("right!")
    else:
        print("wrong!")
    print(num)
num = 2
while num < len(event):
    score(num)
    num += 1
print(winnings/(len(event)-2))
