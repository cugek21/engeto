#seznam zamestnancu
zamestnanci = [
    'František', 'Bruno',
    'Anna', 'Jakub',
    'Klára', 'Anežka',
    'Anežka', 'Anežka'
]

#zjisti posledni index
posledni_index = len(zamestnanci) - 1

#vypis index 2
print('Na indexu 2 je: ', zamestnanci[2])

#vypis posledni index
print('Na', posledni_index, 'indexu je:', zamestnanci[posledni_index])

#vypis interval 2 - 5
print('V intervalu od 2 do 5 je:', zamestnanci[2:6])

#vypis kazdy treti
print('Každý třetí člen je:', zamestnanci[::3])