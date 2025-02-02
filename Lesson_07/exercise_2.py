vstup = 'Ahoj všem'

def zdvojnasob_vsechny_znaky(zadani):
    double = ''
    for str in zadani:
        double = double + (str * 2)
    return double

vysledek = zdvojnasob_vsechny_znaky(vstup)

print(vysledek)