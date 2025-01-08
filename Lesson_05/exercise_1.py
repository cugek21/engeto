slova = []

while len(slova) < 3:
    slovo = input('Zadej slovo ze 4 písmen:')
    if slovo in slova:
        print('Slovo {} už je uložené'.format(slovo))
    elif len(slovo) != 4:
        print('Slovo není dlouhé čtyři znaky')
    else:
        slova.append(slovo)
print('Už mám uložená tři slova')
print(slova)