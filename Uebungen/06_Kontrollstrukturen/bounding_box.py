### Uebung 6: Bounding Box

punkte = [
    {'name': 'A', 'ost': 2600100, 'nord': 1200200},
    {'name': 'B', 'ost': 2601500, 'nord': 1201000},
    {'name': 'C', 'ost': 2599800, 'nord': 1199500},
    {'name': 'D', 'ost': 2600800, 'nord': 1200600},
    {'name': 'E', 'ost': 2602000, 'nord': 1198000},
]

bbox = {'ost_min': 2600000, 'ost_max': 2601000,
        'nord_min': 1200000, 'nord_max': 1201000}


# Ausgabe der Punkte
for p in punkte:
    print (p)

# Überprüfen und zählen welche Punkte in der Box liegen
count = 0
for p in punkte:
    if (bbox['ost_min'] <= p['ost'] <= bbox['ost_max'] and
        bbox['nord_min']<= p['nord']<= bbox ['nord_max']):
        print (f"Punkt {p["name"]} liegt in der Box")
        count += 1
    else:
        print (f"Punkt {p["name"]}liegt ausserhalb der Box")
        
print (f"In der Box liegen {count} Punkte")







# # Ausgabe der Punkte
# for p in punkte:
#     print (p) 

# # Überprüfen, ob oder welche Punkte innerhalb der Bounding Box liegen
# for p in punkte:
#     if (bbox['ost_min'] <= p['ost'] <= bbox['ost_max'] and
#             bbox['nord_min'] <= p['nord'] <= bbox['nord_max']):
#         print(f"Punkt {p['name']} liegt innerhalb der Bounding Box.")
#     else:
#         print(f"Punkt {p['name']} liegt außerhalb der Bounding Box.")
        
# # Zählen, wie viele Punkte innerhalb der Bounding Box liegen
# count = 0
# for p in punkte:
#     if (bbox['ost_min'] <= p['ost'] <= bbox['ost_max'] and
#             bbox['nord_min'] <= p['nord'] <= bbox['nord_max']):
#         count += 1 
# print(f"Anzahl der Punkte innerhalb der Bounding Box: {count}")



