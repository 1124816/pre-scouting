import pickle
import numpy as np
import pandas as pd
import tbapy

#event_code = "2017alhu"
#tba = tbapy.TBA('w4sdTrGh4f4ueC0pfm5ZceCZp3yM3I0SRsJLrn1oblRowvr3Zx2UbcXQpaWnZSpK')
def genBase(event_code, tba):

    teams = tba.event_teams(event_code)
    #teams = tba.event_teams(event_code)
    i = 0
    while i < len(teams):
        teams[i] = teams[i].json
        i+=1

    teams = pd.DataFrame(teams)

    team_info = []
    for i in teams.key:
        team_info.append(tba.team(i).json)
    alldata = pd.DataFrame(team_info)
    data = alldata

    data = data.drop('website', axis=1)
    data = data.drop('state_prov', axis=1)
    data = data.drop('postal_code', axis=1)
    data = data.drop('nickname', axis=1)
    data = data.drop('name', axis=1)
    data = data.drop('motto', axis=1)
    data = data.drop('location_name', axis=1)
    data = data.drop('lng', axis=1)
    data = data.drop('lat', axis=1)
    data = data.drop('home_championship', axis=1)
    data = data.drop('gmaps_url', axis=1)
    data = data.drop('gmaps_place_id', axis=1)
    data = data.drop('country', axis=1)
    data = data.drop('city', axis=1)
    data = data.drop('address', axis=1)

    data = data.set_index('key')

    opr = tba.event_oprs(event_code)
    opr = opr.json
    opr = pd.DataFrame(opr)


    data = data.join(opr)

    finals = tba.event_alliances(event_code)
    final_picks = []
    for i in finals:
        final_picks.append(i.picks)
    final_picks = [item for sublist in final_picks for item in sublist]

    data['final'] = data.index.isin(final_picks)
    team_events = []

    for i in data.index:
        events = []
        tb_events = tba.team_events(i)
        for e in tb_events:
            events.append(e.json)
        team_events.append(events)

    yearly_events = []
    for i in team_events:
        events = []
        for p in i:
            if p['year'] == 2017 and (p['event_type'] == 0 or p['event_type'] == 1):
                events.append(p)
        yearly_events.append(events)
    team_events = yearly_events

    count = []
    for i in team_events:
        count.append(len(i))

    data['num_comps'] = count
    data['rookie_year'] = 2017 - data['rookie_year']


    event = tba.event_matches(event_code)

    teams = tba.event_teams(event_code)

    rotorspermatch = []
    teamstotal = []
    teamspermatch = []

    finished = []
    for i in event:
        if i['score_breakdown']:
             finished.append(i.json)



    for i in finished:
        for r in teams:
            for p in i['alliances']['red']['team_keys']:
                if r['key'] == p:
                    teamspermatch.append(1)
                    break
            else:
                teamspermatch.append(0)

        teamstotal.append(teamspermatch)
        score = 0
        if i['score_breakdown']['red']['rotor2Engaged'] : score += 3
        if i['score_breakdown']['red']['rotor3Engaged'] : score += 4
        if i['score_breakdown']['red']['rotor4Engaged'] : score += 7

        rotorspermatch.append([score])
        teamspermatch = []

        for b in teams:
            for p in i['alliances']['blue']['team_keys']:
                if b['key'] == p:
                    teamspermatch.append(1)
                    break
            else:
                teamspermatch.append(0)
        teamstotal.append(teamspermatch)
        teamspermatch = []

        score = 0
        if i['score_breakdown']['blue']['rotor2Engaged'] : score += 3
        if i['score_breakdown']['blue']['rotor3Engaged'] : score += 4
        if i['score_breakdown']['blue']['rotor4Engaged'] : score += 7

        rotorspermatch.append([score])

    right = np.matrix(rotorspermatch)
    left = np.matrix(teamstotal)
    x,resid,rank,s = np.linalg.lstsq(left,right)
    num = 0
    end_array = []
    while num < len(teams):
        end_array.append([teams[num]["key"], float(x[num])+1])
        num += 1
    end_array = pd.DataFrame(end_array)
    end_array.columns = ['key', 'gears']
    end_array = end_array.set_index('key')
    data = data.join(end_array)


    event = tba.event_matches(event_code)

    teams = tba.event_teams(event_code)

    rotorspermatch = []
    teamstotal = []
    teamspermatch = []

    finished = []
    for i in event:
        if i['score_breakdown']:
             finished.append(i)



    for i in finished:
        for r in teams:
            for p in i['alliances']['red']['team_keys']:
                if r['key'] == p:
                    teamspermatch.append(1)
                    break
            else:
                teamspermatch.append(0)

        teamstotal.append(teamspermatch)
        score = 0
        if i['score_breakdown']['red']['touchpadFar'] == "ReadyForTakeoff" : score += 1
        if i['score_breakdown']['red']['touchpadMiddle'] == "ReadyForTakeoff" : score += 1
        if i['score_breakdown']['red']['touchpadNear'] == "ReadyForTakeoff" : score += 1

        rotorspermatch.append([score])
        teamspermatch = []

        for b in teams:
            for p in i['alliances']['blue']['team_keys']:
                if b['key'] == p:
                    teamspermatch.append(1)
                    break
            else:
                teamspermatch.append(0)
        teamstotal.append(teamspermatch)
        teamspermatch = []

        score = 0
        if i['score_breakdown']['blue']['touchpadFar'] == "ReadyForTakeoff" : score += 1
        if i['score_breakdown']['blue']['touchpadMiddle'] == "ReadyForTakeoff" : score += 1
        if i['score_breakdown']['blue']['touchpadNear'] == "ReadyForTakeoff" : score += 1


        rotorspermatch.append([score])

    right = np.matrix(rotorspermatch)
    left = np.matrix(teamstotal)
    #print(left.shape)
    #print(right.shape)
    x,resid,rank,s = np.linalg.lstsq(left,right)
    num = 0

    end_array = []
    while num < len(teams):
        end_array.append([teams[num]["key"], float(x[num])+1])
        num += 1
    end_array = pd.DataFrame(end_array)
    end_array.columns = ['key', 'rope']
    end_array = end_array.set_index('key')
    #end_array
    data = data.join(end_array)
    data.to_pickle(event_code + "pandas" + ".p")
    return data
