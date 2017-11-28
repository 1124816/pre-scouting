import tbapy
import os

tba = tbapy.TBA(os.environ['TBAKEY'])

events = tba.event_matches('2017alhu')

event = []

for p in events:
    if p['comp_level'] == 'qm':
        event.append(p)

final = [0]*len(event)

for i in event:
    final[i['match_number']-1] = i.alliances['red']['team_keys'] + i.alliances['blue']['team_keys']
#print(number)

scoutlist = [0]*len(final)

x = 0
while x < len(final):
    if 'frc4924' in final[x]:
        y = x-1
        team = {}
        final[x].remove('frc4924')
        for p in final[x]:
            team[p] = 4
        #print(team)
        while y >= 0:
            for i in final[x]:
                if i in final[y] and team[i] > 0:
                    #print('scout team ' + i + ' in match ' + str(number[y]))
                    #if y == 8:
                    #    print(team)
                    #    print(i)
                    #    print(x)
                    if scoutlist[y] == 0:
                        scoutlist[y]=[i]
                    else:
                        scoutlist[y].append(i)
                    team[i]-=1
            y-=1
    x+=1

maxscout = 0
for i in scoutlist:
    if i == 0:i=[]
    if len(i) > maxscout:
        maxscout = len(set(i))
    print(len(set(i)))
print(scoutlist)
print("Max: " + str(maxscout))
