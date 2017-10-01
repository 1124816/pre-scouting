import tbapy

tba = tbapy.TBA(input('key'))

events = tba.event_matches('2017alhu')

event = []

for p in events:
    if p['comp_level'] == 'qm':
        event.append(p)

final = []

for i in event:
    #print(i.alliances['red']['team_keys'])
    final.append(i.alliances['red']['team_keys'] + i.alliances['blue']['team_keys'])

x = 0
while x < len(final):
    if 'frc4924' in final[x]:
        y = x
        team = {}
        final[x].remove('frc4924')
        for p in final[x]:
            team[p] = 6
        while y >= 0:
            for i in team.keys():
                if i in final[y] and team[i] > 0:
                    print('scout team ' + i + ' in match ' + str(y+1))
                    team[i]-=1
            y-=1
    x+=1

