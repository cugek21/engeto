def je_prvocislo(cislo: int, prvocisla: tuple) -> bool:

    return cislo in prvocisla

def generuj_interval_prvocisel(stop: int) -> tuple:
    vysledek = []
    for cislo in range(2,(stop+1)):
        list_delitelu = range(2,cislo)
        for delitel in list_delitelu:
            if cislo % delitel == 0:
                break
        else:
            vysledek.append(cislo)
    return tuple(vysledek)

print(
    je_prvocislo(23, generuj_interval_prvocisel(30)),
    je_prvocislo(233, generuj_interval_prvocisel(300)),
    je_prvocislo(146, generuj_interval_prvocisel(300)),
    sep="\n"
)
