import tbapy

tba = tbapy.TBA('frc4924:test:v1.4')

events = tba.event_matches('2017flwp')
event = []
for p in events:
    if p['comp_level'] == 'qm':
        event.append(p)
 
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
