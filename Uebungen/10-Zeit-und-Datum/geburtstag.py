import datetime

datum_eingabe = input("Gib ein Datum ein (TT.MM.JJJJ): ")

datum = datetime.datetime.strptime(datum_eingabe, "%d.%m.%Y")

wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

wochentag = datum.weekday()

print("Der Wochentag ist:", wochentage[wochentag])
