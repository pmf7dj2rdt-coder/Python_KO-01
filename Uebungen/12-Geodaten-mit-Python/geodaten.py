

import geopandas as gpd
import pandas as pd
import folium


# CSV laden
df = pd.read_csv("messpunkte.csv")

# DataFrame in GeoDataFrame umwandeln: Ost/Nord → Geometrie
gdf = gpd.GeoDataFrame(
    df, 
    geometry=gpd.points_from_xy(df["ost"], df["nord"]),
    crs="EPSG:2056")                                         # LV95

# Koordinaten umprojezieren
gdf_wgs84 = gdf.to_crs("EPSG:4326")

# Zentrum der Karte auf den Mittelpunkt der Punkte setzen
mitte = gdf_wgs84.geometry.union_all().centroid



# Karte zentrieren
karte = folium.Map(
    location=[mitte.y, mitte.x],
    zoom_start=10,
    tiles="https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/3857/{z}/{x}/{y}.jpeg",        # Woher die Karten kommen
    attr="swisstopo",)

# Alle Messpunkte als Marker hinzufügen
for _, row in gdf_wgs84.iterrows():                             # For-Schleife
    folium.Marker(
        location=[row.geometry.y, row.geometry.x],
        tooltip=f"{row['name']}: {row['hoehe']} m.ü.M."
    ).add_to(karte)

# Speichern und öffnen
karte.save("messpunkte.html")

print("Karte gespeichert als messpunkte.html")

