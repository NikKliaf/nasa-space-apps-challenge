import csv

filename = 'Electric_Vehicle_Charging_Stations.csv'
keys = ('Station Name', 'New Georeferenced Column')
records = []

with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        records.append({key: row[key] for key in keys})
print(records[0])

for record in records:
    longitude, latitude = record['New Georeferenced Column'].split("(")[-1].split(")")[0].split()
    record['longitude'] = float(longitude)
    record['latitude'] = float(latitude)

print(records[0])
import folium
from folium.plugins import FastMarkerCluster, MarkerCluster

map = folium.Map(location=[41.5025, -72.699997], zoom_start=9, max_zoom=10)

cluster = MarkerCluster().add_to(map)

for record in records:
    coords = (record['latitude'], record['longitude'])
    folium.Marker(coords, popup=record['Station Name']).add_to(cluster)

map.save('map.html')
