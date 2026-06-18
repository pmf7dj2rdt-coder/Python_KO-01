def nameneingabe():
    while True: 
        try:
            name = str(input("Bitte Nutzername eingeben: "))
            if name.isdigit():
                raise ValueError          
            break
        
        except ValueError:
            print("Ungültiger Wert")
    if str.startswith(name, ("A","a","Ä","ä")):
        print("Toll, du bist im Alphabet ganz vorn")
    print("Schleife ist fertig")
    return name

def beguessung(name):
    print(f"Hallo {name}")

name = nameneingabe()
beguessung(name)


# Musterlösung
def beguessung(name):
    if name.lower() .startswith("a"):                                           #lower macht, dass er auch wenn der Name gross geschrieben wird angezeigt (nicht nur mit kleinem a)
        print(f"Hallo{name}, toll, Du bist im Alphabet ganz vorne")
    else:
        print(f"Hallo {name}, Du bist im Alphabet leider wieter hinten")
    
def nameneingabe():
    while True: 
        try:
            name = str(input("Bitte gib deinen Namen eingeben: "))
            if len(name) == 0:
                raise Exception ("Der Name darf nicht leer sein")
                
            for i in range(10):
                if str(i)in name:
                    raise Exception ("Der Name darf keine Zahl enthaltnen!")
            break
        
        except Exception as e:
            print(e)
            
    return name



name = nameneingabe()
beguessung(name)



