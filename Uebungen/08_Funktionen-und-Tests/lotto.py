import random

def lottoziehung():
    zahlen = set()

    while len(zahlen) < 6:
        zahl = random.randint(1, 42)
        zahlen.add(zahl)

    return zahlen


def tipps_eingeben():
    tipps = set()

    while len(tipps) < 6:
        try:
            zahl = int(input(f"Gib Tipp {len(tipps) + 1} ein: "))

            if zahl < 1 or zahl > 42:
                print("Die Zahl muss zwischen 1 und 42 sein.")
            elif zahl in tipps:
                print("Diese Zahl hast du schon eingegeben.")
            else:
                tipps.add(zahl)

        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")

    return tipps


tipps = tipps_eingeben()

durchlaeufe = 0

while True:
    ziehung = lottoziehung()
    durchlaeufe += 1

    if ziehung == tipps:
        break

print("Deine Tipps:", tipps)
print("Gewinnziehung:", ziehung)
print("Du hattest nach", durchlaeufe, "Durchlaeufen 6 Richtige.")