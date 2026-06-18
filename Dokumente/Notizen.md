# Notizen Python Modul

## Tag 1

### Instalationen
- Python
- GitHub
- Git-scm (Homebrew)
- Visual Studio Code
- Python Extention Pack (im Visual Studio unter Extentions)
- Pytest Tool (im Terminal eingeben *pip3 install pytest* --> *export PATH="/Users/MichelleKunzSchule/Library/Python/3.14/bin:$PATH"*)
- Requests

### Git mit Desktop verknüpfen
1. Terminal öffnen
2. ***cd*** und der Pfad vom Speicherort. Bsp ***/Users/MichelleKunzSchule/Desktop***
3. Enter
4. ***Git clone*** und der Speicherort von der Datei anschliessend eingeben. Bsp. ***https://github.com/pmf7dj2rdt-coder/Python_KO-01.git***


### Tools
#### Gitignore
Mit dem File ***.gitignore*** könen Folders oder einzelne Files ausgeblendet werden. 

#### Darstellung von Codes
```python
import time
print("Hello word")
```
- [ ] Checkliste erstellen
- [ ] Nochmals Checkliste erstellen


#### Ordner hinzufügen
mit dem code ***git status*** sieht man im Terminal (von Visual Studio Code) welche Ordner schon verknüpft sind und welche noch nicht. Wenn es Rot ist muss man (Bsp .gitignore): ***git add .gitignore***

#### Git in den Browser hochladen
- Den Status anzeigen lassen: **git status**
- Alles hinzugüfhen: **git add -A**
- Den Aktuellen Stand meines Projektes in Git speichern: **git commit -m "Was gemacht wurde"**
- Um es nicht nur Lokal zu haben muss man es pushen: **git push**

### Python
Datei mit Endung .py gibt automatisch eine Python Datei, dass es als Python einfach lesbar ist.
Debugging Mode --> Macht das es das Programm schritt für schritt laufen lässt.
Breakpoints (Roter Pkt am Rand) setzen und es führt es nur bis dahin aus
Mit dem # Zeichen können im Python Dokument Notzien gemacht werden, die nicht ausgeführt werden sollen.

break steht dann unterbricht es.
contuinoue überspringt restliche Anweisungsblöcke

Funktionen immer eine Klammer. In Klammer sind Parameter drin ("l","") "l" Das was sie ersetzten soll und "" womit sie ersetzt wird.
Wenn man count und dann = Zahl dann wird nur diese Anzahl Zahlen ersetzt. Default: Alle

Schleifen Funktionen sind **for** und **while**

Funktionen beginnen mit **def** dann die Funktion() und immer Klammer dahinter. Wenn man einen Wert zurück haben will, dann am Schluss **return = Funktion** Aufrufen kann man sie mit **result = Funktion()**.

## Importe
- import time      # Für Zeit-Funktionen, z.B. aktuelle Zeit oder Zeit messen
- import math      # Für Mathematik, z.B. Wurzel, Pi, Sinus
- import pytest    # Für Tests von Python-Code
- import string    # Für Zeichenketten-Hilfen, z.B. Alphabet oder Satzzeichen
- import random    # Für Zufallszahlen
- import datetime  # Für Datum und Uhrzeit
- import locale    # Für Länder-/Spracheinstellungen, z.B. deutsches Datumsformat


Wenn Befehl nicht funktioniert schauen das ich im Terminal im richtigen Ordner bin. 
- Entweder neues Terminal öffenne 
- Oder diesen Befehl eingeben und zum richtigen Pfad navigieren **cd Uebungen/12-Geodaten-mit-Python**