import csv
import random
from math import floor

import geopy.distance


def calculate_distance(lat_a, long_a, lat_b, long_b):
    coords_1 = (lat_a, long_a)
    coords_2 = (lat_b, long_b)
    km = geopy.distance.distance(coords_1, coords_2)
    return km / 1.852  # to nm


def suggest_route(range_start, range_end):
    suggestions = []
    with open(
            'static/us-airports.csv') as airports:  # Conditions that satisfy these flight suggestions
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
            nm = round(float(str(distance).replace(" km", "")) / 1.852, 1)
            if nm >= int(range_start) and nm <= int(range_end):
                suggestions.append([starting_icao, airfield_icao, nm])
    return suggestions

def format(suggestions_list: list):
    formatted = []
    for s in suggestions_list:
        start = s[0]
        end = s[1]
        d = s[2]
        formatted.append(start + " -> " + end + " " + str(d) + " nm")
    return formatted

test = suggest_route(100, 300)
