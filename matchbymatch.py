import tbapy

tba = tbapy.TBA('frc4924:test:v1.4')

events = tba.event_matches('2017flwp')
teams = tba.event_teams('2017flwp')
event = []
for p in events:
    if p['comp_level'] == 'qm':
        event.append(p)
num = 0
finished = []
winnings = 0
while num < len(event):
    finished = []
    for i in event:
        if i['match_number'] < num:
            finished.append(i)

    score = {}
    for i in teams:
        score[i['key']] = {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}

    for i in finished:
        for r in i['alliances']['red']['teams']:
            if r in score:
                score[r]["matches"].append(i['score_breakdown']['red']['totalPoints']/3)
            else:
                score[r] = {'matches' : [], 'score' : 0, 'error': [], 'errorsum': 0}
                score[r]["matches"].append(i['score_breakdown']['red']['totalPoints']/3)
        for b in i['alliances']['blue']['teams']:
            if b in score:
                score[b]["matches"].append(i['score_breakdown']['blue']['totalPoints']/3)
            else:
                score[b] = {'matches' : [], 'score' : 0, 'error': [], 'errorsum': 0}
                score[b]["matches"].append(i['score_breakdown']['blue']['totalPoints']/3)

    for i in score:
        if len(score[i]['matches']) > 0:
            score[i]['score'] = sum(score[i]['matches'])/len(score[i]['matches'])
        else:
            score[i]['score'] = 60

    count = 0
    while count < 500:
        for i in score:
            score[i]['matches'] = []

        for i in finished:
            rest = 0
            rerror = 0
            best = 0
            berror = 0
            for r in i['alliances']['red']['teams']:
                rest += score[r]['score']
            rerror = i['score_breakdown']['red']['totalPoints']-rest
            for r in i['alliances']['red']['teams']:
                score[r]['matches'].append(score[r]['score']+(rerror*(score[r]['score']/(20*i['score_breakdown']['red']['totalPoints']+0.000001))))

            for b in i['alliances']['blue']['teams']:
                best += score[b]['score']
            berror = i['score_breakdown']['blue']['totalPoints']-best
            for b in i['alliances']['blue']['teams']:
                score[b]['matches'].append(score[b]['score']+(berror*(score[b]['score']/(20*i['score_breakdown']['blue']['totalPoints']+0.000001))))
        for i in score:
            if len(score[i]['matches']) > 0:
                score[i]['score'] = sum(score[i]['matches'])/len(score[i]['matches'])
            else:
                score[i]['score'] = 60

        count += 1

    redscore = score[event[num]['alliances']['red']['teams'][0]]['score']+score[event[num]['alliances']['red']['teams'][1]]['score']+score[event[num]['alliances']['red']['teams'][2]]['score']
    bluescore = score[event[num]['alliances']['blue']['teams'][0]]['score']+score[event[num]['alliances']['blue']['teams'][1]]['score']+score[event[num]['alliances']['blue']['teams'][2]]['score']
    #redscore = opr[event[num]['alliances']['red']['teams'][0][3:]]+opr[event[num]['alliances']['red']['teams'][1][3:]]+opr[event[num]['alliances']['red']['teams'][2][3:]]
    #bluescore = opr[event[num]['alliances']['blue']['teams'][0][3:]]+opr[event[num]['alliances']['blue']['teams'][1][3:]]+opr[event[num]['alliances']['blue']['teams'][2][3:]]
    rguess = bluescore < redscore
    uguess = event[num]['score_breakdown']['blue']['totalPoints'] < event[num]['score_breakdown']['red']['totalPoints']
    if rguess == uguess:
        winnings += 1
        print ("right!")
    else:
        print("wrong!")
    num += 1
    print(num)
print(winnings/len(event))
