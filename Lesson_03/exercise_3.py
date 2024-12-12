#vstupni data
cisla_1 = (1, 1, 2, 3, 4)
cisla_2 = (5, 6, 7, 7, 8)

#zmena na sety
set_1 = set(cisla_1)
set_2 = set(cisla_2)

#sjednoceni
sjednocene_hodnoty = set_1.union(set_2)

#vypis
print('Sjednocené hodnoty ze zadání:', sjednocene_hodnoty)