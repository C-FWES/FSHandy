import csv

def get_frequencies(icao):
    extracted_frequencies = []
    with open('static/airport-frequencies.csv', encoding="utf8") as frequencies:
        reader = list(csv.reader(frequencies))
        for i in range(len(reader)):
            if reader[i][2] == icao:
                extracted_frequencies.append([reader[i][3], reader[i][5]])
            if reader[i-1] == icao and reader[i+1] != icao:
                break

    return extracted_frequencies