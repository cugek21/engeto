import random

moznosti = ['kamen', 'nuzky', 'papir']

while True:
    hrac = input('Vyber kamen, nuzky nebo papir:').lower().strip()
    if hrac not in moznosti:
        print('Taková možnost není.')
    else:
        break

pc = random.choice(moznosti)
print(f'Počítač: {pc}')

if hrac == pc:
    print("Nerozhodně!")
elif (hrac == 'kamen' and pc == 'nuzky') or \
    (hrac == 'papir' and pc == 'kamen') or \
    (hrac == 'nuzky' and pc == 'papir'):
    print('Vyhrál jsi!')
else:
    print('Prohál jsi!')