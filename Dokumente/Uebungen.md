# Erledigte Übungen

## 06-Kontrollstrukturen
> **Übung: Pyramide**
> `pyramide.py`
>
> - Versuche mit möglichst wenig Code folgende Muster auf dem Bildschirm anzuzeigen
> - Nutze z.B. `'X' * 2` um das X zu vervielfachen
> - Falls benötigt, ist `\n` ein Zeilenumbruch
> - Versuche, die Höhe der Pyramiden über eine Variable festzulegen
>
> ```text
> X
> XX
> XXX
> XXXX
> XXXXX
> ```
>
> ```text
>     X
>    XX
>   XXX
>  XXXX
> XXXXX
> ```
>
> ```text
>     X
>    XXX
>   XXXXX
>  XXXXXXX
> XXXXXXXXX
> ```

***

> **Übung: Schachbrett**
> `schach.py`
>
> - Versuche, die Bezeichnung der einzelnen Felder eines Schachbretts auf dem Bildschirm anzuzeigen
>
> _Achtung:_
>
> - Die Spalten sind alphabetisch **auf**steigend von `a` bis `h`
> - Die Zeilen sind numerisch **ab**steigend von `8` bis `1`
>
> _Tipp:_
>
> - alle Buchstaben des Alphabets erhältst Du z.B. so: `abc = string.ascii_lowercase`
> - nutze z.B. `sorted` mit `reverse=True` für absteigende Sortierung
>
> _Beispiel:_
>
> ```text
> a8 b8 c8 d8 e8 f8 g8 h8
> a7 b7 c7 d7 e7 f7 g7 h7
> a6 b6 c6 d6 e6 f6 g6 h6
> a5 b5 c5 d5 e5 f5 g5 h5
> a4 b4 c4 d4 e4 f4 g4 h4
> a3 b3 c3 d3 e3 f3 g3 h3
> a2 b2 c2 d2 e2 f2 g2 h2
> a1 b1 c1 d1 e1 f1 g1 h1
> ```

***

> **Übung: Summe**
> `summe.py`
>
> Berechne mit einer `for`-Schleife die Summe der Elemente in der Liste `[1, 2, 3, 4, 5, 6]`.
>
> _Tipp_:
> Innerhalb eines Anweisungsblocks können wir auf Variablen von ausserhalb des Blocks zugreifen und diese verändern. Dazu wird eine Variable vor dem Block initialisiert (z.B. `summe = 0`) und dieser Wert bei jedem Schleifendurchlauf um die aktuelle Zahl erhöht.
> **Übung: Debugging**
> `debugging.py`
>
> Lege eine Datei mit dem Namen `debugging.py` an und kopiere den folgenden Code hinein:
>
> ```python
> zahl = 1
>
> while zahl <= 10:
>    zahl = zahl - 0.0123456
>
> print("Schleife fertig")
> ```
>
> Wenn man das Script ausführt, hängt es in einer Endlosschleife fest.
> In diesem Fall ist es recht offensichtlich, woran das liegt. Aber in komplexeren Scripts würde hier der Debugger helfen.
> Wenn man z.B. den Verdacht hat, dass das Abbruchkriterium einer Schleife nie erreicht wird, kann man einen _Breakpoint_ innerhalb der Schleife setzen. So können wir beispielsweise den Wert der Variablen "zahl" in jedem Schleifendurchlauf beobachten.
> Um einen Breakpoint zu setzen, die Maus links neben der Zeilennummer bewegen. Es erscheint ein schwach roter Punkt. Wenn man ihn anklickt, wird er hellrot und bleibt fix neben der Zeile. Dieser rote Punkt bedeutet, dass in dieser Zeile die Ausführung des Codes gestoppt wird und man die aktuellen Variablenwerte anschauen kann, bevor der Code weiter ausgeführt wird. Wenn ein Breakpoint innerhalb einer Schleife gesetzt ist, wird der Code bei jedem Schleifendurchlauf an der Stelle unterbrochen, so dass man die aktuellen Variablenwerte anschauen kann.

> **Übung: Bounding Box**
> `bounding_box.py`
>
> Du hast eine Liste von Messpunkten mit LV95-Koordinaten. Filtere mit einer Schleife und einer Bedingung alle Punkte heraus, die innerhalb eines bestimmten Ausschnitts (Bounding Box) liegen.
>
> ```python
> punkte = [
>     {'name': 'A', 'ost': 2600100, 'nord': 1200200},
>     {'name': 'B', 'ost': 2601500, 'nord': 1201000},
>     {'name': 'C', 'ost': 2599800, 'nord': 1199500},
>     {'name': 'D', 'ost': 2600800, 'nord': 1200600},
>     {'name': 'E', 'ost': 2602000, 'nord': 1198000},
> ]
>
> bbox = {'ost_min': 2600000, 'ost_max': 2601000,
>         'nord_min': 1200000, 'nord_max': 1201000}
> ```
>
> - Iteriere über die Liste `punkte`
> - Prüfe mit `if` und `and`, ob ein Punkt innerhalb der Bounding Box liegt
> - Gib die Namen der Punkte innerhalb der Box aus
> - Zähle, wie viele Punkte innerhalb und wie viele ausserhalb liegen

## 07-Benutzereingaben
> **Übung: Benutzereingaben**
> `kreis.py`
>
> Schreibe ein Skript, das folgendes kann:
>
> - Der Benutzer soll einen Radius als Parameter eingeben
> - Das Skript berechnet Durchmesser, Umfang und Fläche des Kreises
>
> _Tipps_:
>
> - Entscheide selber, ob Du `input()` oder `sys.argv[]` einsetzen möchtest.
> - Importiere das Modul `math` und nutze die Konstante `pi` für die Kreiszahl.

***

> **Übung: Koordinateneingabe**
> `koordinaten_input.py`
>
> Schreibe ein Skript, das den Benutzer nach LV95-Koordinaten (Ostwert und Nordwert) fragt und diese dann formatiert ausgibt.
>
> - Gib die Koordinaten im Format `E 2'600'000 / N 1'200'000` aus.
> - Gib zusätzlich aus, ob der Punkt grob innerhalb der Schweiz liegt (LV95: ca. E 2'480'000–2'840'000, N 1'070'000–1'300'000).
>
> _Tipps:_
>
> - Der Userinput ist immer ein String - denke an `float()` oder `int()` zum Umwandeln.
> - Zahlen lassen sich mit f-strings und dem Format-Code `:,.0f` mit Tausendertrennzeichen ausgeben:
>   `f"{wert:,.0f}"` - ersetze das Komma bei Bedarf mit einem Apostroph über `str.replace()`.

## 08-Funktionen-und-Test
> **Übung: Tests schreiben**
> `test_kreis.py`
>
> 1. Stelle sicher, dass `kreis_funktion.py` vorhanden ist.
> 2. Erstelle eine neue Datei `test_kreis.py`.
> 3. Schreibe mindestens drei Testfunktionen für `calc_diameter`, `circumference` und `calc_area`.
> 4. Führe die Tests mit `pytest test_kreis.py` aus.
> 5. Verändere eine Funktion in `kreis_funktion.py` absichtlich falsch - und prüfe, ob pytest den Fehler erkennt.

***

> **Übung: Lottosimulation**
> `lotto.py`
>
> Wie gross ist die Wahrscheinlichkeit, im Schweizer Zahlenlotto 6 Richtige zu haben?
>
> _Tipps:_
>
> - Definiere eine Funktion, die eine Lottoziehung (6 aus 42) simulieren kann.
> - `random.randint(1, 42)` liefert eine Zufallszahl zwischen 1 und 42. (Es braucht ein `import random`.)
> - Denk daran, dass eine Zahl nur einmal gezogen werden kann. Erinnerst Du Dich an `set()`?
> - Erstelle eine einfache Benutzereingabe für die Abgabe der 6 Tipps.
> - Führe Deine Funktion in einer `while`-Schleife solange aus, bis die sechs Zufallszahlen mit den Tipps übereinstimmen.
> - Zähle die Durchläufe.

## 09 Dateien

> **Übung: Textfile lesen und schreiben**
> `namen.py`
>
> 1. Erzeuge eine neue Textdatei mit dem Namen `personen.txt`.
> 2. Schreibe einige Personen in die Liste im Format _Vorname_ _Nachname_.
> 3. Versuche zuerst, die Namen aus der Datei `personen.txt` zu laden und nur die Nachnamen auf dem Bildschirm zu zeigen.
> 4. Wenn das klappt, schreibe die Nachnamen in alphabetischer Reihenfolge in die Datei `nachnamen_alphabetisch.txt`.
>
> _Tipps:_
>
 > - Schritt 1 und 2 kannst Du auch manuell ohne Programmieren machen, oder Du lädst die Datei [hier herunter](https://raw.githubusercontent.com/hansmannj/py-tutorial/master/resources/personen.txt).
 > - Nutze `.strip()` um Zeilenumbrüche zu eliminieren.
 > - Mit `.split(" ")` können Vor- und Nachname in eine Liste mit zwei Einträgen aufgeteilt werden, die nachher über ihren Index `[]` angesprochen werden können.
 > - `with open` mit dem Parameterwert `"w"` öffnet einen Schreibzugriff (**w**rite) auf eine Datei. Eine bestehende Datei wird überschrieben, eine neue automatisch angelegt.
 > - Verwende `write()` oder `writelines()` um die Zeilen in das Textfile zu schreiben. Denke an die Zeilenumbrüche `\n`.

***

> **Übung: CSV mit Koordinaten lesen und schreiben**
> `koordinaten_csv.py`
>
> In der Geomatik werden Koordinaten häufig als CSV-Dateien ausgetauscht. In dieser Übung liest Du eine solche Datei ein, berechnest die Höhendifferenz zwischen den Punkten und schreibst das Ergebnis in eine neue Datei.
>
> Lade die Datei `messpunkte.csv` herunter (oder lege sie manuell an):
>
> ```text
> name,ost,nord,hoehe
> Zimmerwald,2602025,1191761,898
> Bantiger,2606806,1202974,947
> Gurten,2600378,1196252,858
> Chasseral,2571227,1220302,1606
> Napf,2638131,1205962,1406
> ```
>
> 1. Lies die Datei `messpunkte.csv` zeilenweise ein.
> 2. Überspringe die Kopfzeile (`name,ost,nord,hoehe`).
> 3. Trenne jede Zeile mit `.split(",")` in ihre Bestandteile auf.
> 4. Berechne für jeden Punkt die Höhendifferenz zum tiefsten Punkt in der Liste.
> 5. Schreibe die Ergebnisse in eine neue Datei `hoehendifferenzen.csv` mit dem Format `name,hoehe,differenz`.
>
> _Tipps:_
>
> - Denke daran, die Höhe mit `float()` in eine Zahl umzuwandeln.
> - Um den tiefsten Punkt zu finden, kannst Du zuerst alle Höhen in eine Liste speichern und dann `min()` verwenden.
> - Runde die Differenz mit `round()` auf eine Dezimalstelle.
>
> _Die `messpunkte.csv` begegnet euch in Kapitel 12 wieder - dann laden wir sie mit zwei Zeilen GeoPandas und stellen alle Punkte auf einer interaktiven Karte dar. Lohnt sich also, die Datei zu behalten._

## 10 Zeit und Datum
> **Übung: Geburtstag**
> `geburtstag.py`
>
> Schreibe ein Programm mit interaktiver Benutzereingabe, das folgende Fragen beantwortet:
>
> - An welchem Wochentag wurdest Du geboren?
> - An welchem Wochentag feierst Du Deinen 30. Geburtstag?

***

> **Übung: Datensatz-Alter**
> `datensatz_alter.py`
>
> In der Geomatik wird oft angegeben, wann ein Datensatz erstellt oder zuletzt aktualisiert wurde.
>
> Schreibe ein Skript, das:
>
> 1. Den Benutzer nach dem Aufnahmedatum eines Datensatzes fragt (Format: `TT.MM.JJJJ`).
> 2. Berechnet, wie viele Tage der Datensatz alt ist.
> 3. Eine Warnung ausgibt, falls der Datensatz älter als 365 Tage ist:
>    `"Achtung: Datensatz ist älter als 1 Jahr – bitte auf Aktualität prüfen."`
>
> _Tipp:_ Nutze `try`/`except` um ungültige Datumseingaben abzufangen.

## 11 Web und APIs
> **Übung: Koordinatentransformation**  
> `koordinaten.py`
>
> Das Gebäude von swisstopo hat die WGS84-Koordinaten 46.928°N 7.452°E. Unser Schulungsgebäude liegt bei der LV95-Koordinate 2600052m, 1198762m.
>
> - Wie weit sind die beiden Gebäude (Luftlinie) voneinander entfernt?
> - Runde das Resultat auf 10m genau
>
> _Tipps:_
>
> - gehe schrittweise vor
> - programmiere zuerst die Transformation
> - berechne danach die Distanz (Pythagoras)
>
***
> **Übung: Webdienste BGDI**  
> `adresse.py`
>
> 1. Studiere die [Dokumentation zu den Webdiensten der Bundes-Geodateninfrastruktur](https://docs.geo.admin.ch/access-data/search.html#search).
> 2. Versuche zu einer beliebigen Adresse die Koordinaten zu erhalten.
>    Beispiel-URL: [SearchServer?searchText=wabern&type=locations](https://docs.geo.admin.ch/access-data/search.html#examples)


## Geodaten mit Python
> **Übung: Messpunkte auf der Karte**
> `geodaten.py`
>
> 1. Lade `messpunkte.csv` (aus Kapitel 8) und erstelle daraus einen GeoDataFrame in LV95.
> 2. Projiziere die Punkte nach WGS84.
> 3. Erstelle eine folium-Karte mit den Messpunkten. Zeige im Tooltip Name und Höhe an.
> 4. Speichere die Karte als `messpunkte.html` und öffne sie im Browser.

***

> **Übung: Räumlicher Join mit Messgebieten**
> `geodaten_zonen.py`
>
> 1. Lade zusätzlich `messgebiete.geojson` als GeoDataFrame.
> 2. Führe einen räumlichen Join (`gpd.sjoin`) durch: welcher Messpunkt liegt in welcher Zone?
> 3. Gib aus, welche Punkte keiner Zone zugeordnet werden konnten.
> 4. Zeige die Zonen und Punkte zusammen auf einer folium-Karte. Färbe die Zonen unterschiedlich ein (`folium.GeoJson`).
>
> _Tipp:_ Mit `how="left"` im `sjoin` bleiben auch Punkte ohne Zone im Ergebnis (mit `NaN` in der Zonenspalte).

## QGIS Python
> **Übung: Kantone auswerten**
> `qgis_kantone.py`
>
> 1. Öffne QGIS und die Python-Konsole.
> 2. Lade den Kantonsgrenz-Layer von swisstopo mit dem Code aus dem POC oben.
> 3. Zeige alle Spaltennamen mit `layer.fields().names()`.
> 4. Gib die 5 flächengrössten Kantone aus (berechne die Fläche mit `feature.geometry().area()`).
> 5. Selektiere alle Kantone, die an den Kanton Bern grenzen.
>
> _Tipp:_ Mit `layer.fields().names()` siehst Du die genauen Spaltennamen - Gross-/Kleinschreibung zählt.

***

> **Übung: Messpunkte laden**
> `qgis_messpunkte.py`
>
> 1. Lade `messpunkte.csv` direkt in QGIS (Layer → Layer hinzufügen → Getrennte Textdatei).
> 2. Öffne die Python-Konsole.
> 3. Gib für jeden Messpunkt Name und Höhe aus.
> 4. Berechne mit Python die Höhendifferenz zwischen dem höchsten und tiefsten Punkt.
