### Uebung 1: Benutzereingaben

r = float(input("Bitte den Radius eingeben1"))
import math

d = 2 * r
U = 2 * r * math.pi
A = r**2 * math.pi

print(f"Durchmesser: {d}")
print(f"Umfang: {U}")
print(f"Fläche:{A}")
