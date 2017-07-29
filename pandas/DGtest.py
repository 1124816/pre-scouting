import DatabaseGen
import tbapy

event_code = "2017alhu"
tba = tbapy.TBA('w4sdTrGh4f4ueC0pfm5ZceCZp3yM3I0SRsJLrn1oblRowvr3Zx2UbcXQpaWnZSpK')
print(DatabaseGen.genBase(event_code, tba))
#print(tba.event_oprs(event_code).oprs['frc4924'])
