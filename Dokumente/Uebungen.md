# Übungen

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