veta = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'
samohlasky = 'aeiouáéíóú'
souhlasky = 'bcčdďfghjklmnňprřsštťvzžcdž'
vysledek = {'samohlasky': 0, 'souhlasky': 0}

for letter in veta:
    if not letter.isalpha():
        continue
    elif letter.lower() in samohlasky:
        vysledek['samohlasky'] += 1
    elif letter.lower() in souhlasky:
        vysledek['souhlasky'] += 1

print(f'Počet samohlásek: {vysledek['samohlasky']} | Počet souhlásek: {vysledek['souhlasky']}')