ovoce = {'jablko', 'banan', 'citron', 'pomeranc'}

print('Dostupné ovoce:', ', '.join(ovoce))

vyber = True
while vyber:
    vyber = input('VYBER Z DOSTUPNÉHO OVOCE:')
    if vyber in ovoce:
        print(f'Bezva, {vyber} je v nabídce')
        vyber = False
    else:
        print(f'{vyber} není v nabídce')