import folium

min_lon, max_lon = 22.88, 23
min_lat, max_lat = 40.6, 40.7

m = folium.Map(
    max_bounds=True,
    location=[40.640184, 22.935334],
    zoom_start=13,
    min_lat=min_lat,
    max_lat=max_lat,
    min_lon=min_lon,
    max_lon=max_lon,
    min_zoom=13
)


m.save('test.html')