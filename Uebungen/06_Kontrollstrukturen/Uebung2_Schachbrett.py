### Uebung 1: Schachbrett (06 Kontrollstrukturen)

import string

schachbuchstaben = string.ascii_lowercase[:8]

for i in range (8,0,-1):
    for j in schachbuchstaben:
        print(f"{i}{j}", end=" ")
    print()