### Uebung 1: Pyramide (06 Kontrollstrukturen)

# rechtsschief
for i in range(1, 6): 
    print("x" * i)
    
# linksschief
for i in range(1,6):
    print(" " * (5 - i) + "x" * i)
        
# symmetrisch
for i in range(1,6):
    print(" " * (5 - i) + "x" * (2*i - 1))  
    