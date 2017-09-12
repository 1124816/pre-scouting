import DatabaseGen
import tbapy
import os

event_code = "2017alhu"
tba = tbapy.TBA(os.environ['TBAKEY'])
print(DatabaseGen.genBase(event_code, tba))
#print(tba.event_oprs(event_code).oprs['frc4924'])
