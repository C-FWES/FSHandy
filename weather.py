
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


# test_runways =  [
#     {
#       "length_ft": 14572,
#       "width_ft": 150,
#       "ident1": "13R",
#       "ident2": "31L"
#     },
#     {
#       "length_ft": 11351,
#       "width_ft": 150,
#       "ident1": "04L",
#       "ident2": "22R"
#     },
#     {
#       "length_ft": 10000,
#       "width_ft": 150,
#       "ident1": "13L",
#       "ident2": "31R"
#     },
#     {
#       "length_ft": 8400,
#       "width_ft": 200,
#       "ident1": "04R",
#       "ident2": "22L"
#     }
#   ]
# test_metar = "KJFK 031551Z 35021G29KT 10SM -RA FEW024 BKN036 OVC046 10/07 A2966 RMK AO2 PK WND 36029/1550 RAB10 SLP042 P0000 T01000067"
# test_reccomend = reccommend_runway(test_runways, test_metar)
# print(test_reccomend)