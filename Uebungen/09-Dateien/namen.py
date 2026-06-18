
# Datei mit Projekt verknüpfen
datei = r"/Users/MichelleKunzSchule/Desktop/Python_KO-01/Uebungen/08_Funktionen-und-Tests/personen.txt"

with open(datei, "r") as lesezugriff:       # Dateien lesen und öffnen
    inhalt = lesezugriff.readlines()
print(inhalt)


nachnamen = []                              # Nur Nachnamen anzeigen lassen

for zeile in inhalt:
    teile = zeile.strip() .split(" ")
    nachnamen.append(teile[1])
    
print("Nachnamen:")
for name in nachnamen:
    print(name)


nachnamen.sort()                            # Nachnamen nach Alphabet sortieren

print("Nachnamen alphabetisch sortiert:")
for name in nachnamen:
    print(name)
    
    
    
# Neues File mit einer erzeugten Datei erstellen.
ausgabe_datei = r"/Users/MichelleKunzSchule/Desktop/Python_KO-01/Uebungen/09-Dateien/nachnamen_alphabetisch.txt"

nachnamen.sort()

with open(ausgabe_datei, "w") as schreibzugriff:
    for name in nachnamen:
        schreibzugriff.write(name + "\n")