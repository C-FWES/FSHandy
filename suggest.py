import csv
import random
import geopy.distance


def calculate_distance(lat_a, long_a, lat_b, long_b):
    coords_1 = (lat_a, long_a)
    coords_2 = (lat_b, long_b)
    km = geopy.distance.distance(coords_1, coords_2)
    return km / 1.852  # to nm


def suggest_route():
    suggestions = []
    with open(
            'static/us-airports.csv') as airports:  # Conditions that satisfy these flight suggestions: 100-250 nautical miles
        reader = list(csv.reader(airports))
        starting_airfield = random.choice(reader)
        starting_icao = starting_airfield[1]
        starting_lat = float(starting_airfield[4])
        starting_long = float(starting_airfield[5])
        data = list(csv.reader(airports))
        for i in range(1, len(reader)):
            airfield_icao = reader[i][1]
            airfield_lat = float(reader[i][4])
            airfield_long = float(reader[i][5])
            distance = calculate_distance(starting_lat, starting_long, airfield_lat, airfield_long)
            if distance >= 100 and distance <= 300:
                suggestions.append([starting_icao, airfield_icao])
    return suggestions

test = suggest_route()
print(test)
