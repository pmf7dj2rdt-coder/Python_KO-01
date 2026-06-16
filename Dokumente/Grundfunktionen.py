zahl1: float = 1
zahl2: float = 2
result: float = zahl1 + zahl2 
print("Das Ergebnis ist:", result) 
print(f"Das Ergebnis von {zahl1} + {zahl2} ist: {result}")

# Mit dem "#"Zeichen können Notzien gemacht werden, die nicht ausgeführt werden.

2 * 3 + 4

4 - ( 5 / 6 ) 

5 // 3                  # Ganzzahlige Division

5 % 3                   # Modulo - Rest der Division

int(4.3923903)          # Umwandlung in einen Integer (Nicht gerundet, sondern abgeschnitten)

text1 = "test"
text1 * 4
text1 [2]               # Zugriff auf das 3. Zeichen (Index beginnt bei 0)    
text1 [0:3]             # Zugriff auf die ersten 3 Zeichen (Index beginnt bei 0, das letzte Zeichen wird nicht mitgezählt)
text1 [2:]              # Zugriff auf alle Zeichen ab dem 3. Zeichen (Index beginnt bei 0)
text1 [:3]              # Zugriff auf die ersten 3 Zeichen (Index beginnt bei 0, das letzte Zeichen wird nicht mitgezählt)
text1 [-1]              # Zugriff auf das letzte Zeichen (Index beginnt bei 0, das letzte Zeichen wird nicht mitgezählt)
text1 [-3:]             # Zugriff auf die letzten 3 Zeichen (Index beginnt bei 0, das letzte Zeichen wird nicht mitgezählt)

text1 = "3.333"
float(text1)            # Umwandlung in einen Float

#Kommt immer draufan wie man es schreibt, auf die Groß- und Kleinschreibung achten.
#Bei jeder neuen Zuweisung wird der alte Wert überschrieben.

dummy = 5 > 3           # Vergleichsoperatoren, geben immer einen Wahrheitswert zurück (True oder False)

text = "Hallo"
"l" in text             # Überprüft, ob das Zeichen "l" in der Variable text enthalten ist, gibt True zurück
"x" in text             # Überprüft, ob das Zeichen "x" in der Variable text enthalten ist, gibt False zurück

# Datentypen: int, float, str, bool
# Integer ist eine ganze Zahl, Float ist eine Kommazahl.
# Float ist eine Kommazahl, die auch Exponentialschreibweise verwenden kann (z.B. 1e-5 für 0.00001).
# String ist eine Liste von Buchstaben.
# Boolean ist ein Wahrheitswert, der entweder True oder False sein kann.

week = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
type(week)              # Überprüft den Datentyp der Variable week, gibt list zurück
week [1]                # Kommt Dienstag raus.
"Montag" in week        # Überprüft, ob "Montag" in der Liste week enthalten ist, gibt True zurück
week.pop(7)             # Entfernt das letzte Element der Liste (Sonntag) und gibt es zurück. Speziell für den Datentyp list. 
week.append("Sonntag")  # Fügt das Element "Sonntag" am Ende der Liste week hinzu. Speziell für den Datentyp list.
week = sorted(week)     # Sortiert die Liste week alphabetisch und gibt eine neue sortierte Liste zurück. Überschreibt den alten Wert von week. 
week.remove("Montag")   # Entfernt das erste Vorkommen von "Montag".

lt = sorted ("swisstopo")  # Sortiert die Zeichen in dem String "swisstopo" alphabetisch und gibt eine neue sortierte Liste zurück.

                        # Es kann in einer Liste auch mehere Einträge Doppelt geben
set(lt)                 # Erstellt eine Menge (Set) aus der Liste lt, wodurch doppelte Einträge entfernt werden. Gibt eine neue Menge zurück.
len(lt)                 # Gibt die Anzahl der Elemente in der Liste lt zurück. In diesem Fall 10, da es 10 Zeichen in "swisstopo" gibt, auch wenn einige davon doppelt sind.

set ("Landestopografie") & set ("swisstopo")  # Gibt die Schnittmenge der beiden Mengen zurück, also die Zeichen, die in beiden Strings enthalten sind. In diesem Fall {'s', 't', 'o', 'p'}.
set ("Landestopografie") ^ set ("swisstopo")  # Gibt die symmetrische Differenz der beiden Mengen zurück, also die Zeichen, die in einen der Strings, aber nicht in beiden enthalten sind.
lt_set = set(lt)         # Erstellt eine Menge (Set) aus der Liste lt und speichert sie in der Variable lt_set. Doppelte Einträge werden entfernt.
lt_set.add("d")          # Fügt das Element "d" zur Menge lt_set hinzu. Wenn "d" bereits in der Menge enthalten ist, hat diese Operation keine Auswirkungen.
# Sets sind praktisch für das rechnen mit Lottozahlen.

bern2d = (600000, 200000)  # Ein Tupel, bestehend aus zwei Zahlen. Es ist unveränderlich (immutable), d.h. die Werte können nicht geändert werden.
type(bern2d)              # Überprüft den Datentyp der Variable bern2d, gibt tuple zurück
bern2d[0]                # Zugriff auf das erste Element des Tupels bern2d, gibt 600000 zurück

bern3d = (600000, 200000, 500)  # Ein Tupel, bestehend aus drei Zahlen. Es ist unveränderlich (immutable), d.h. die Werte können nicht geändert werden.
type(bern3d)              # Überprüft den Datentyp der Variable bern3d, gibt tuple zurück
bern3d[2]                # Zugriff auf das dritte Element des Tupels bern3d, gibt 500 zurück

# Wenn Tupels definiert sind, könnens sie nicht mehr geändert werden, nur noch überschrieben. 

# dictionary # Nachschlageverzeichnis
anrede = {"de":"Hoi", "fr":"Salut", "it":"Ciao"}  
anrede["fr"]
user_lang = "de"
user.lang[f"{anrede[user_lang]} Kurt"] # Gibt "Hoi Kurt" zurück, da user_lang den Wert "de" hat und anrede["de"] den Wert "Hoi" zurückgibt. 

# Schleifen um den gleichen Code mehrmals auszuführen (Bsp Liste mit vielen Koord. und man will alle Nordkorrd. eizel haben.)
# Hier müssten z.B. Koordinaten von 10 Orten stehen.
for i in range(1,10):      # Für jedes Element i in der Liste week, führe den folgenden Code aus:
    print(i)               # Gibt das Element an der Position i in der Liste week zurück. In diesem Fall werden die Wochentage von Dienstag bis Sonntag ausgegeben, da die Indizes von 1 bis 9 gehen (Index 0 ist Montag).
    print(hallo)
    print(something)
    
    print("Fertig")         # Dieser Code wird nach der Schleife nur einmal ausgeführt, da er nicht eingerückt ist.
    
print("x"/n)                # Mit /n kann man einen Zeilenumbruch erzwingen.