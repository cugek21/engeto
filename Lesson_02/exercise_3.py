# zamestnanci
zamestnanci = ['František', 'Anna', 'Jakub', 'Klára']
               
#vypis je
print('Zaměstnanci na začátku:', zamestnanci)

#kopie listu
zamestnanci_a = zamestnanci.copy()

#pridani novych jmen
zamestnanci_a.append('Bruno')
zamestnanci_a.append('Anežka')

#vypis
print('Nová jména přidána:', zamestnanci_a)

#kopie listu
zamestnanci_b = zamestnanci.copy()

#vlozeni na index
zamestnanci_b.insert(1, 'Bruno')

#vypis
print('Nová jména vložena:', zamestnanci_b)