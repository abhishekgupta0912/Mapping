import folium as f
import pandas as pd

file = pd.read_csv("valcano.txt")

lat = list(file["LAT"])
lon = list(file["LON"])
name = list(file["NAME"])

map = f.Map(location=[25.460780, 78.583011], zoom_start=6, tiles="Stamen Terrain")

fgv = f.FeatureGroup(name="Valcanoes")
for nam, lt, ln in zip(name, lat, lon):
    fgv.add_child(f.Marker(location=[lt, ln], popup=nam, icon=f.Icon(color="green")))

fgp = f.FeatureGroup(name="Population")
fgp.add_child(f.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                        style_function=lambda x: {
                            'fillColor ': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <=
                                                                                                            x[
                                                                                                                'properties'][
                                                                                                                'POP2005'] < 20000000 else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(f.LayerControl())

map.save("Map.html")
