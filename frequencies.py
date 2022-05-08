import csv

def get_frequencies(icao):
    icao = icao.upper()
    extracted_frequencies = []
    with open('static/airport-frequencies.csv', encoding="utf8") as frequencies:
        reader = list(csv.reader(frequencies))
        for i in range(len(reader)):
            if reader[i][2] == icao:
                extracted_frequencies.append([reader[i][3], reader[i][5]])
            if reader[i-1] == icao and reader[i+1] != icao:
                break
    return extracted_frequencies

def format_freq(freqs):
    formatted = []
    for f in freqs:
        result = f[0] + " " + f[1]
        formatted.append(result)
    return formatted