### Uebung 2 Koordinateingabe

o = float(input("Ostwert(E) eingeben"))
n = float(input("Nordwert(N) eingeben)"))

o_formation = f"{o:,.0f}" .replace(",","'")
n_formation = f"{n:,.0f}" .replace(",","'")

print(f"E{o_formation}/ N {n_formation}")

if 2840000 <= o <= 2480000 and 1300000 <= n <= 1070000:
    print(f"Der Punkt {o_formation } / {n_formation} liegt in der Schweiz")
else:
    print(f"Der Punkt {o_formation } / {n_formation} liegt nicht in der Schweiz")
