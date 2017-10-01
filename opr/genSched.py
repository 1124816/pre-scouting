import tbapy

tba = tbapy.TBA('w4sdTrGh4f4ueC0pfm5ZceCZp3yM3I0SRsJLrn1oblRowvr3Zx2UbcXQpaWnZSpK')

events = tba.event_matches('2017alhu')

for p in events:
    if p['comp_level'] == 'qm':
        event.append(p)

for i in event:
    print(i)
