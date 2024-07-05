import os
import sys
import django
import csv
from collections import defaultdict

# SET THE PATH OF THE APPLICATION HERE
sys.path.append('/Users/jakobuspretorius/Desktop/CM3035_Advanced_Web_Development/Midterm/Application/airlines')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airlines.settings')
django.setup()

from airlineapp.models import *

# EMPTY ALL THE EXISTING TABLES
Equipment_list.objects.all().delete()
Routes.objects.all().delete()
Airlines.objects.all().delete()
Airports.objects.all().delete()
Countries.objects.all().delete()
Planes.objects.all().delete()

# SET UP THE VARIABLES FOR THE LOCATIONS OF THE DATA FILES
countries_data_file = '/Users/jakobuspretorius/Desktop/CM3035_Advanced_Web_Development/Midterm/Application/data/csv/countries.csv'
planes_data_file = '/Users/jakobuspretorius/Desktop/CM3035_Advanced_Web_Development/Midterm/Application/data/csv/planes.csv'
airlines_data_file = '/Users/jakobuspretorius/Desktop/CM3035_Advanced_Web_Development/Midterm/Application/data/csv/airlines.csv'
airports_data_file = '/Users/jakobuspretorius/Desktop/CM3035_Advanced_Web_Development/Midterm/Application/data/csv/airports.csv'
routes_data_file = '/Users/jakobuspretorius/Desktop/CM3035_Advanced_Web_Development/Midterm/Application/data/csv/routes.csv'

# SET UP THR VARIABLES TO BE USED AS PART OF THE READ
countries = set()
planes = set()
airlines = set()
airports = set()
routes = set()

# READ AND POPULATE: COUNTRIES
with open(countries_data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        countries.add((row[0], row[1], row[2]))

for country in countries:
    row = Countries.objects.create(name=country[0], iso_code=country[1], dafif_code=country[2])

# READ AND POPULATE: PLANES
with open(planes_data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        planes.add((row[0], row[1], row[2]))

for plane in planes:
    row = Planes.objects.create(name=plane[0], iata=plane[1], icao=plane[2])

# READ AND POPULATE: AIRLINES
with open(airlines_data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        airlines.add((row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

for airline in airlines:
    country_object = Countries.objects.filter(name=airline[5]).first()
    row = Airlines.objects.create(name=airline[0], alias=airline[1], iata=airline[2], icao=airline[3], callsign=airline[4], country=country_object, active=airline[6])

# READ AND POPULATE: AIRPORTS
with open(airports_data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        airports.add((row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13]))

for airport in airports:
    country_object = Countries.objects.filter(name=airport[2]).first()
    row = Airports.objects.create(name=airport[0], city=airport[1], country=country_object, iata=airport[3], icao=airport[4], latitude=airport[5], longitude=airport[6], altitude=airport[7], timezone=airport[8], dst=airport[9], tz_db=airport[10], type=airport[11], source=airport[12])

# READ AND POPULATE: ROUTES
with open(routes_data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        routes.add((row[0], row[2], row[4], row[6], row[7], row[8]))

## have done the variable naming a little differently here because there are many foreign key assignments, so just wanted to make it clearer what everything was.
for route in routes:
    route_airline_object = (Airlines.objects.filter(iata = route[0]) | Airlines.objects.filter(icao = route[0])).first()
    route_from_object = (Airports.objects.filter(iata = route[1]) | Airports.objects.filter(icao = route[1])).first()
    route_to_object = (Airports.objects.filter(iata = route[2]) | Airports.objects.filter(icao = route[2])).first()
    route_codeshare = route[3]
    route_stops = route[4]

    route_equipment = route[5].split(" ")

    row = Routes.objects.create(airline_id = route_airline_object, from_airport = route_from_object, to_airport = route_to_object, codeshare = route_codeshare, stops = route_stops)

    for equip in route_equipment:
        induvidual_equip = (Planes.objects.filter(iata = equip) | Planes.objects.filter(icao = equip)).first()
        row.equipment.add(induvidual_equip)