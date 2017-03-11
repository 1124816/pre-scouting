import tbapy

tba = tbapy.TBA('frc4924:test:v1.4')

events = tba.event_matches('2017flwp')
event = []
for p in events:
    if p['comp_level'] == 'qm':
        event.append(p)
opr = tba.event_stats('2017flwp')['oprs']
num = 0
finished = []
winnings = 0
while num < len(event):
    for i in event:
        if i['match_number'] < num:
            finished.append(i)

    score = {'frc386': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc3653': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc6388': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc125': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc1523': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc6404': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc6225': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc2556': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc6001': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc4481': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc1251': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc5819': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc348': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc233': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc179': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc4592': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc6038': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc1744': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc694': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc263': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc2641': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc4471': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc2383': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc2152': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc59': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc6669': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc21': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc4517': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc5196': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc5557': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc6685': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc2914': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc6435': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc5558': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc5872': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc5993': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc6416': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc6468': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc5472': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc79': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc6686': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc6743': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc3410': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc5329': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc5949': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc5243': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}, 'frc5410': {'matches': [], 'score': 0, 'error': [], 'errorsum': 0}}

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
#
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
            #        print("blue wins")
print(winnings/len(event))
#for i in finished:
#    rest = 0
#    rerror = 0
#    best = 0
#    berror = 0
#    for r in i['alliances']['red']['teams']:
#        rest += score[r]['score']
#    rerror = (i['score_breakdown']['red']['totalPoints']-rest)**2
#    for r in i['alliances']['red']['teams']:
#        score[r]['error'].append(rerror)
#
#    for b in i['alliances']['blue']['teams']:
#        best += score[b]['score']
#    berror = (i['score_breakdown']['blue']['totalPoints']-best)**2
#    for b in i['alliances']['blue']['teams']:
#        score[b]['error'].append(berror)
#
#for i in score:
#    score[i]['errorsum'] = sum(score[i]['error'])/len(score[i]['error'])

#winnings = 0
#rights = []
#wrongs = []
#for i in finished:
#    redscore = score[i['alliances']['red']['teams'][0]]['score']+score[i['alliances']['red']['teams'][1]]['score']+score[i['alliances']['red']['teams'][2]]['score']
#    bluescore = score[i['alliances']['blue']['teams'][0]]['score']+score[i['alliances']['blue']['teams'][1]]['score']+score[i['alliances']['blue']['teams'][2]]['score']
#    #redscore = opr[i['alliances']['red']['teams'][0][3:]]+opr[i['alliances']['red']['teams'][1][3:]]+opr[i['alliances']['red']['teams'][2][3:]]
#    #bluescore = opr[i['alliances']['blue']['teams'][0][3:]]+opr[i['alliances']['blue']['teams'][1][3:]]+opr[i['alliances']['blue']['teams'][2][3:]]
#    bigerror = score[i['alliances']['red']['teams'][0]]['errorsum']+score[i['alliances']['red']['teams'][1]]['errorsum']+score[i['alliances']['red']['teams'][2]]['errorsum']+score[i['alliances']['blue']['teams'][0]]['errorsum']+score[i['alliances']['blue']['teams'][1]]['errorsum']+score[i['alliances']['blue']['teams'][2]]['errorsum']
#    rguess = bluescore < redscore
#    uguess = i['score_breakdown']['blue']['totalPoints'] < i['score_breakdown']['red']['totalPoints']
#    if rguess == uguess:
#        #print('right!')
#        #print(bigerror)
#        rights.append(bigerror)
#        winnings += 1
#    else:
#        #print('wrong!')
#        #print(bigerror)
#        wrongs.append(bigerror)
#    if bluescore < redscore:
#        #print("red wins")
#        pass
#    else:
#        #print("blue wins")
#        pass
#    if i['score_breakdown']['blue']['totalPoints'] < i['score_breakdown']['red']['totalPoints']:
#        #print("red wins")
#        pass
#    else:
#        #print("blue wins")
#        pass
#    #print(bluescore)
#    #print(i['score_breakdown']['blue']['totalPoints'])
#    #print(redscore)
#    #print(i['score_breakdown']['red']['totalPoints'])
#rightsum = sum(rights)/len(rights)
#leftsum = sum(wrongs)/len(wrongs)
#print('right')
#print(rightsum)
#print('wrong')
#print(leftsum)
#
#print(winnings/len(finished))
#
