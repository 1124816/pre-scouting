
def onlyEvent(team):
    pass

def firstEvent(team):
    pass

 events = []
 for event in events:
     firstTeams = {}
     onlyTeams = {}
     oldTeams = {}
     for team in event:
         if onlyEvent(team):
             onlyTeams[team] = []
         elif firstEvent(team):
             firstTeams[team] = []
        else:
            oldTeams[team] = team
    for match in event:
        score = {}
        
