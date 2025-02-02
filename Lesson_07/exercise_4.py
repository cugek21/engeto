prvni_cislo = 12
druhe_cislo = 16

def najdi_gcd(x1, x2):
    while x2 != 0:
        zbytek_po_deleni = x1 % x2
        x1, x2 = x2, zbytek_po_deleni
    return x1 

print(najdi_gcd(prvni_cislo,druhe_cislo))