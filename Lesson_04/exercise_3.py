vysledek = list()
start = 3
stop = 9
delitel = 3

if isinstance(start, int) and isinstance(stop, int) and isinstance(delitel, int):
    print(f'Zadaný rozsah: <{start}, {stop}>')
    for cislo in range(start,stop):
        if cislo % delitel == 0:
            vysledek.append(cislo)    
    print(f'Čísla dělitelná {delitel}: {vysledek}')
else:
    print('Zadané vstupy musí být čísla.')