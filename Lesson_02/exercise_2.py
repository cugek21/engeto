#user
jmeno = 'Martin'
vaha = 80 #kg
vyska = 2 #m

#vypocet BMI
bmi = vaha / (vyska ** 2)

#kategorie
if bmi < 18.5:
    kategorie = 'Podvýživa'
elif bmi < 25:
    kategorie = 'Zdravá váha'
elif bmi < 30:
    kategorie = 'Mírná nadváha'
elif bmi < 40:
    kategorie = 'Obezita'
elif bmi > 40:
    kategorie = 'Těžká obezita'

#vypis
print(jmeno, 'tvé BMI je', bmi, ', což spadá do kategorie', kategorie, '.')