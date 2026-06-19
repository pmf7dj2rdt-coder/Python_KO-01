#!/usr/bin/env python3
"""
geodaten_zonen_messpunkte.py
- Liest messpunkte.csv (Spalten 'ost','nord', optional 'name','hoehe')
- Liest messgebiete.geojson
- Führt räumlichen Join (Punkt in Zone) durch
- Erstellt Folium-Karte mit swisstopo-WMTS, farbigen Zonen und Punkten (grün=hat Zone, rot=keine Zone)
- Speichert Karte als zonen_messpunkte_map.html
Anpassen: Dateipfade, Spaltennamen, CRS falls nötig.
"""
import random
import pandas as pd
import geopandas as gpd
import folium

# Optional: MarkerCluster für viele Punkte
from folium.plugins import MarkerCluster

# ---------- Einstellungen (anpassen) ----------
punkte_fp = "messpunkte.csv"           # CSV mit Spalten 'ost','nord' (koordinaten in LV95/EPSG:2056)
zonen_fp = "messgebiete.geojson"      # GeoJSON/Other mit Zonen
map_fp = "zonen_messpunkte_map.html"
zone_id_col = "zone_id"
# WMTS Tile-URL (swisstopo Beispiel, Web-Mercator tiles)
wmts_url = "https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/3857/{z}/{x}/{y}.jpeg"
wmts_attr = "swisstopo"

# ---------- 1) CSV einlesen und GeoDataFrame erstellen ----------
df = pd.read_csv(punkte_fp)

# Erwartete Spalten prüfen
required_cols = {"ost", "nord"}
if not required_cols.issubset(df.columns):
    raise KeyError(f"Die CSV muss die Spalten {required_cols} enthalten. Aktuelle Spalten: {list(df.columns)}")

# Erzeuge GeoDataFrame (hier angenommen LV95 / EPSG:2056)
gdf_punkte = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(df["ost"], df["nord"]),
    crs="EPSG:2056"  # anpassen falls nötig
)

if gdf_punkte.empty:
    raise ValueError("Keine Punkte in der CSV vorhanden.")

# ---------- 2) Zonen einlesen ----------
zonen = gpd.read_file(zonen_fp)
if zonen.empty:
    raise ValueError("Zonen-Layer ist leer oder konnte nicht gelesen werden.")
if zonen.crs is None:
    raise ValueError("Zonen-Layer hat kein CRS. Bitte CRS in der Quelldatei setzen oder hier angeben.")

# ---------- 3) Einheitliche CRS für räumliche Operationen ----------
# Konvertiere Zonen in die CRS der Punkte (oder umgekehrt)
if not zonen.crs.equals(gdf_punkte.crs):
    zonen = zonen.to_crs(gdf_punkte.crs)

# ---------- 4) Zone-ID sicherstellen ----------
if zone_id_col not in zonen.columns:
    zonen = zonen.reset_index().rename(columns={"index": zone_id_col})
zonen[zone_id_col] = zonen[zone_id_col].astype(str)

# ---------- 5) Räumlicher Join (Punkt innerhalb Zone) ----------
try:
    sjoined = gpd.sjoin(gdf_punkte, zonen[[zone_id_col, "geometry"]], how="left", predicate="within")
except TypeError:
    # Fallback für ältere geopandas-Versionen die 'op' statt 'predicate' nutzen
    sjoined = gpd.sjoin(gdf_punkte, zonen[[zone_id_col, "geometry"]], how="left", op="within")

# ---------- 6) Auswertung: Punkte ohne Zone ----------
punkte_ohne_zone = sjoined[sjoined[zone_id_col].isna()]

print("Anzahl Punkte insgesamt:", len(sjoined))
print("Anzahl Punkte ohne zugeordnete Zone:", len(punkte_ohne_zone))
if len(punkte_ohne_zone) > 0:
    print("Erste Punkte ohne Zone:")
    cols = [c for c in punkte_ohne_zone.columns if c != "geometry"]
    print(punkte_ohne_zone.head()[cols])

# ---------- 7) Vorbereitung für Folium (WGS84/EPSG:4326) ----------
sjoined_4326 = sjoined.to_crs("EPSG:4326")
zonen_4326 = zonen.to_crs("EPSG:4326")

# Kartenmittelpunkt bestimmen (robust)
union = None
try:
    union = sjoined_4326.geometry.unary_union
except Exception:
    union = zonen_4326.geometry.unary_union

if union is None or union.is_empty:
    # Fallback: Mittelwert der Punkt-Koordinaten
    if len(sjoined_4326) > 0:
        center_lat = sjoined_4326.geometry.y.mean()
        center_lon = sjoined_4326.geometry.x.mean()
    else:
        raise ValueError("Kann kein Zentrum bestimmen (keine Geometrien).")
else:
    center = union.centroid
    center_lat, center_lon = center.y, center.x

# ---------- 8) Folium-Karte erstellen ----------
m = folium.Map(location=[center_lat, center_lon], zoom_start=11, tiles=None)

# WMTS/TileLayer hinzufügen
folium.raster_layers.TileLayer(
    tiles=wmts_url,
    attr=wmts_attr,
    name="swisstopo",
    overlay=False,
    control=True,
    max_zoom=20
).add_to(m)

# Farbzuordnung für Zonen (diskrete Farben)
unique_zone_ids = zonen_4326[zone_id_col].astype(str).unique()
color_map = {zid: "#{:06x}".format(random.randint(0, 0xFFFFFF)) for zid in unique_zone_ids}

def style_function(feature):
    zid = str(feature["properties"].get(zone_id_col, ""))
    return {
        "fillColor": color_map.get(zid, "#ffffff"),
        "color": color_map.get(zid, "#000000"),
        "weight": 1,
        "fillOpacity": 0.5,
    }

# Zonen als GeoJson hinzufügen (Popup/Tooltip mit zone_id)
folium.GeoJson(
    zonen_4326.__geo_interface__,
    name="Zonen",
    style_function=style_function,
    tooltip=folium.GeoJsonTooltip(fields=[zone_id_col], aliases=["Zone:"])
).add_to(m)

# ---------- 9) Punkte hinzufügen ----------
# Wenn viele Punkte vorhanden sind, benutze MarkerCluster für bessere Performance
use_cluster = True
if use_cluster:
    cluster = MarkerCluster(name="Messpunkte").add_to(m)

for idx, row in sjoined_4326.iterrows():
    geom = row.geometry
    if geom is None or geom.is_empty:
        continue
    lat, lon = geom.y, geom.x
    zid = row.get(zone_id_col)
    has_zone = not pd.isna(zid)
    color = "green" if has_zone else "red"
    # Tooltip aus name/hoehe zusammenbauen falls vorhanden
    tooltip_parts = []
    if "name" in row and not pd.isna(row["name"]):
        tooltip_parts.append(str(row["name"]))
    if "hoehe" in row and not pd.isna(row["hoehe"]):
        tooltip_parts.append(f"{row['hoehe']} m.ü.M.")
    tooltip = ": ".join(tooltip_parts) if tooltip_parts else None
    popup_html = f"Punkt index: {idx}<br>Zone: {zid}"
    marker = folium.CircleMarker(
        location=[lat, lon],
        radius=4,
        color=color,
        fill=True,
        fill_opacity=0.9,
        tooltip=tooltip,
        popup=folium.Popup(popup_html, max_width=300)
    )
    if use_cluster:
        marker.add_to(cluster)
    else:
        marker.add_to(m)

folium.LayerControl().add_to(m)

# ---------- 10) Karte speichern ----------
m.save(map_fp)
print(f"Karte gespeichert als: {map_fp}")