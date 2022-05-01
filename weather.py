
def format_runways(runways):
    formatted = []
    for r in runways:
        length = str(r['length_ft'])
        ident_1 = r['ident1']
        ident_2 = r['ident2']
        result_str = ident_1 + "/" + ident_2 + ": " + length + " feet"
        formatted.append(result_str)
    return formatted

def reccommend_runway(runways, metar): #21
    reccomendation = ''
    runway_numbers = []
    metar_sections = metar.split()
    wind = metar_sections[2]
    wind_bearing = 0
    if wind[:3] == 'VRB':
        wind_bearing = 0
    else:
        wind_bearing = int(wind[:3])
    for r in runways:
        ident_1 = int(r['ident1'][:2] + "0")
        ident_2 = int(r['ident2'][:2] + "0")
        runway_numbers.append(ident_1)
        runway_numbers.append(ident_2)
    difference = 1000
    for n in runway_numbers:
        temp = abs(n - wind_bearing)
        if temp < difference:
            difference = temp
            reccomendation = str(n)
    return reccomendation
