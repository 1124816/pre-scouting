import tbapy
import os

tba = tbapy.TBA(os.environ['TBAKEY'])

event = tba.event_matches('2017code')
opr = tba.event_oprs('2017code').json['oprs']

finished = []
for i in event:
    if i['comp_level'] == 'qm':
         finished.append(i.json)

score = {}

for i in finished:
    for r in i['alliances']['red']['team_keys']:
        if r in score:
            score[r]["matches"].append(i['score_breakdown']['red']['totalPoints']/3)
        else:
            score[r] = {'matches' : [], 'score' : 0, 'error': [], 'errorsum': 0}
            score[r]["matches"].append(i['score_breakdown']['red']['totalPoints']/3)
    for b in i['alliances']['blue']['team_keys']:
        if b in score:
            score[b]["matches"].append(i['score_breakdown']['blue']['totalPoints']/3)
        else:
            score[b] = {'matches' : [], 'score' : 0, 'error': [], 'errorsum': 0}
            score[b]["matches"].append(i['score_breakdown']['blue']['totalPoints']/3)

for i in score:
    score[i]['score'] = sum(score[i]['matches'])/len(score[i]['matches'])

count = 0
#while count < 5000:
#    for i in score:
#        score[i]['matches'] = []
#
#    for i in finished:
#        rest = 0
#        rerror = 0
#        best = 0
#        berror = 0
#        for r in i['alliances']['red']['teams']:
#            rest += score[r]['score']
#        rerror = i['score_breakdown']['red']['totalPoints']-rest
#        for r in i['alliances']['red']['teams']:
#            score[r]['matches'].append(i['score_breakdown']['red']['totalPoints']*(score[r]['score']/(i['score_breakdown']['red']['totalPoints']+0.000001)))
#
#        for b in i['alliances']['blue']['teams']:
#            best += score[b]['score']
#        berror = i['score_breakdown']['blue']['totalPoints']-best
#        for b in i['alliances']['blue']['teams']:
#            score[b]['matches'].append(i['score_breakdown']['blue']['totalPoints']*(score[b]['score']/(i['score_breakdown']['blue']['totalPoints']+0.000001)))
while count < 80:
    for i in score:
        score[i]['matches'] = []

    for i in finished:
        rest = 0
        rerror = 0
        best = 0
        berror = 0
        for r in i['alliances']['red']['team_keys']:
            rest += score[r]['score']
        rerror = i['score_breakdown']['red']['totalPoints']-rest
        for r in i['alliances']['red']['team_keys']:
            score[r]['matches'].append(score[r]['score']+(rerror*(score[r]['score']/(50*(i['score_breakdown']['red']['totalPoints']+0.1)))))

        for b in i['alliances']['blue']['team_keys']:
            best += score[b]['score']
        berror = i['score_breakdown']['blue']['totalPoints']-best
        for b in i['alliances']['blue']['team_keys']:
            score[b]['matches'].append(score[b]['score']+(berror*(score[b]['score']/(50*(i['score_breakdown']['blue']['totalPoints']+0.1)))))
#
    for i in score:
        score[i]['score'] = sum(score[i]['matches'])/len(score[i]['matches'])

    count += 1
    #print(score['frc141']['score'])

#print(score)
#while True:
#    matcha = input("lolz")
#    match = tba.match('2017flwp_qm'+matcha)
#    print('red')
#    redscore = score[match['alliances']['red']['teams'][0]]['score']+score[match['alliances']['red']['teams'][1]]['score']+score[match['alliances']['red']['teams'][2]]['score']
#    print(redscore)
#    print('blue')
#    bluescore = score[match['alliances']['blue']['teams'][0]]['score']+score[match['alliances']['blue']['teams'][1]]['score']+score[match['alliances']['blue']['teams'][2]]['score']
#    print(bluescore)
#    if bluescore < redscore:
#        print("red wins")
#    else:
#        print("blue wins")
#for i in score:
#    score[i]['matches'] = []
#    score[i]['score'] = 60
#print(score)
for i in finished:
    rest = 0
    rerror = 0
    best = 0
    berror = 0
    for r in i['alliances']['red']['team_keys']:
        rest += score[r]['score']
    rerror = (i['score_breakdown']['red']['totalPoints']-rest)**2
    for r in i['alliances']['red']['team_keys']:
        score[r]['error'].append(rerror)

    for b in i['alliances']['blue']['team_keys']:
        best += score[b]['score']
    berror = (i['score_breakdown']['blue']['totalPoints']-best)**2
    for b in i['alliances']['blue']['team_keys']:
        score[b]['error'].append(berror)

for i in score:
    score[i]['errorsum'] = sum(score[i]['error'])/len(score[i]['error'])

winnings = 0
rights = []
wrongs = []
for i in finished:
    redscore = score[i['alliances']['red']['team_keys'][0]]['score']+score[i['alliances']['red']['team_keys'][1]]['score']+score[i['alliances']['red']['team_keys'][2]]['score']
    bluescore = score[i['alliances']['blue']['team_keys'][0]]['score']+score[i['alliances']['blue']['team_keys'][1]]['score']+score[i['alliances']['blue']['team_keys'][2]]['score']
    #redscore = opr[i['alliances']['red']['team_keys'][0]]+opr[i['alliances']['red']['team_keys'][1]]+opr[i['alliances']['red']['team_keys'][2]]
    #bluescore = opr[i['alliances']['blue']['team_keys'][0]]+opr[i['alliances']['blue']['team_keys'][1]]+opr[i['alliances']['blue']['team_keys'][2]]
    #bigerror = score[i['alliances']['red']['team_keys'][0]]['errorsum']+score[i['alliances']['red']['team_keys'][1]]['errorsum']+score[i['alliances']['red']['team_keys'][2]]['errorsum']+score[i['alliances']['blue']['team_keys'][0]]['errorsum']+score[i['alliances']['blue']['team_keys'][1]]['errorsum']+score[i['alliances']['blue']['teams'][2]]['errorsum']
    rguess = bluescore < redscore
    uguess = i['score_breakdown']['blue']['totalPoints'] < i['score_breakdown']['red']['totalPoints']
    print(bluescore)
    print(redscore)
    if rguess == uguess:
        print('right!')
        print(i['match_number'])
        #print(bigerror)
        #rights.append(bigerror)
        winnings += 1
    else:
        print('wrong!')
        print(i['match_number'])
        #print(bigerror)
        #wrongs.append(bigerror)
    if bluescore < redscore:
        print("red wins")
        pass
    else:
        print("blue wins")
        pass
    if i['score_breakdown']['blue']['totalPoints'] < i['score_breakdown']['red']['totalPoints']:
        #print("red wins")
        pass
    else:
        #print("blue wins")
        pass
    #print(bluescore)
    #print(i['score_breakdown']['blue']['totalPoints'])
    #print(redscore)
    #print(i['score_breakdown']['red']['totalPoints'])
#rightsum = sum(rights)/len(rights)
#leftsum = sum(wrongs)/len(wrongs)
#print('right')
#print(rightsum)
#print('wrong')
#print(leftsum)

print(winnings/len(finished))
