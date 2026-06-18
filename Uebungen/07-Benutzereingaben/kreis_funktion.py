### Uebung 3: Benutzereingabe

import math

def check_radius_input():
    """Fetches radius form user input and checks, if it is a valid fload.
    Returns: 
        A float value of the radius form the user input
    """
    while True:
        try:
            # Versuchen, Benutzereingabe ine ine Flieskommazahl 'float' umzuwandeln...
            r = float(input("Bitte einen positiven Radius eingeben"))
            # Wenn das klappt, while SChleife abbrechen, wenn der Radius positiv ist.
            if r < 0:
                raise Exception("Radius darf nicht negativ sein")
            break
        except ValueError:
            # Sonst den User um erneutere Eingabe bitten
            print("Bitte eine Zahl eingeben")
        except Exception:
            print("Bitte eine positive Zahl eingeben")
            
    print("Die while-Schleife ist fertig")
    return r   

def durchmesser(r):
    return r * 2

def flaeche (r):
    return r**2 * math.pi

def umfang(r):
    return 2 * math.pi


radius =check_radius_input()
f = flaeche(radius)

print(f"Die Fläche ist:{f}")    
    
    
