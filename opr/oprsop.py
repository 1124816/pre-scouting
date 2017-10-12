import tbapy
import os

tba = tbapy.TBA(os.environ['TBAKEY'])

event = tba.event_matches('2017alhu')
opr = tba.event_oprs('2017alhu').json['oprs']

finished = []
for i in event:
    if i['comp_level'] == 'qm':
         finished.append(i.json)

finished[0]['alliances']['red']
