import requests

adresse = input("Adresse eingeben (Strasse Hausnummer, PLZ Ort): ")
                
url = "https://api3.geo.admin.ch/rest/services/ech/SearchServer"

parameter = {
    "searchText": adresse,
    "type": "locations"
}

antwort = requests.get(url, params=parameter)
daten = antwort.json()

if len(daten["results"]) > 0:
    treffer = daten["results"][0]
    infos = treffer["attrs"]

    print("Gefundene Adresse:", infos["label"])
    print("Breitengrad:", infos["lat"])
    print("Längengrad:", infos["lon"])
    print("Koordinate X:", infos["x"])
    print("Koordinate Y:", infos["y"])
else:
    print("Keine Adresse gefunden.")
    
