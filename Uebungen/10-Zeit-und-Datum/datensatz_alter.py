from datetime import datetime

while True:
    try:
        eingabe = input("Aufnahmedatum eingeben (TT.MM.JJJJ): ")

        aufnahmedatum = datetime.strptime(eingabe, "%d.%m.%Y")
        heute = datetime.today()

        alter = heute - aufnahmedatum
        tage_alt = alter.days

        print(f"Der Datensatz ist {tage_alt} Tage alt.")

        if tage_alt > 365:
            print("Achtung: Datensatz ist älter als 1 Jahr – bitte auf Aktualität prüfen.")

        break

    except ValueError:
        print("Ungültiges Datum! Bitte im Format TT.MM.JJJJ eingeben.")