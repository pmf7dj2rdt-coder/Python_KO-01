### Uebung 3: Summe (06 Kontrollstrukturen)


Zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Version 1
Summe = 0

for i in Zahlen:
    Summe += i
print("Die Summe der Zahlen von 1 bis 10 ist:", Summe)

# Version 2
Summe = 0

for i in Zahlen:
    Summe += i
print(f"Die Summe der Zahlen {Zahlen} ist:", Summe)

# Version 3
summe = sum(Zahlen)
print(f"Die Summe der Zahlen {Zahlen} ist:", summe)


# Summe += i ist eine Kurzschreibweise für summe = summe + i was konkret bedeutet, dass die aktuelle Summe um den Wert von i erhöht wird. Es ist eine bequeme Möglichkeit, die Summe in einer Schleife zu aktualisieren, ohne die Variable summe jedes Mal neu zu schreiben.