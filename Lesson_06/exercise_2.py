import os

jmena_slozek = 'obrazky', 'texty', 'gify'

for name in jmena_slozek:
    if not os.path.isdir(name):
        os.mkdir(name)
        print(f'Tvořím novou složku: {name}')
    else:
        print(f'Složka {name} již existuje!')

print('Všechny složky existují')