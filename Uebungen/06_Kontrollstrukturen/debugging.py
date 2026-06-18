### Uebung 5: Verzweigungen (06 Kontrollstrukturen)

# Ein gleichheitszeichen ist eine Zuweisung.
# Ein doppeltes gleichheitszeichen ist eine Vergleichsoperation, die überprüft, ob zwei Werte gleich sind.
# Ausrufezeichen Gleich (!=) ist eine Vergleichsoperation, die überprüft, ob zwei Werte ungleich sind.

#| Operator  | Bedeutung                             | Beispiel     |
#| `==`      | ist gleich                            | `"a" == "b"` |
#| `!=`      | ist ungleich                          | `"a" != "b"` |
#| `<`       | ist kleiner als                       | `1 < 2`      |
#| `<=`      | ist kleiner gleich                    | `2 <= 2`     |
#| `>`       | ist grösser als                       | `1 > 2`      |
#| `>=`      | ist grösser gleich                    | `4 >= 3`  |
#| `in`      | ist in einer Collection enthalten     | `"e" in "Hello"` |


for zahl in range[1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9]:
    if zahl == 3:
        print(zahl, "juhee, drei")
    elif zahl == 7:
        print(zahl, "yepee, sieben")
    elif zahl == 9:
        print(zahl, "yes, neun")
    else:
        print(zahl, "eine andere Zahl")
