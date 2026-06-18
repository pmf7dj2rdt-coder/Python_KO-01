
import requests
import math

e = 7.452
n = 46.928

service = "https://geodesy.geo.admin.ch/reframe/wgs84tolv03"

parameter = {"easting": e,
             "northing": n,
             "format": "json"}

response = requests.get(url=service, params=parameter, verify=False)
result = response.json()

print(result["easting"])
print(result["northing"])


# Luftlinie berrechnen
a = 601017.990423179 - 600052                   # Wenn die Distanz negativ ist, funktioniert der Pythagoras nicht.
b = 198762 - 197433.9052806796

distanz = math.sqrt(a**2 + b**2)
print("Die Distanz zwischen den beiden Punkten beträgt {distanz}")

print(round(distanz, -1))