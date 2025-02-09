adresy = [
   "matous@holinka.com",
   "danek11@seznam.cz",
   "rennud15@gmail.com",
   "pepa@centrum.cz"
]

def filtruj_adresy_s_cisly(emaily: list) -> list:
    ciselny_email = []
    for email in emaily:
        for char in email:
            if not char.isnumeric():
                continue
            ciselny_email.append(email)
            break
        
    return ciselny_email

vysledek = filtruj_adresy_s_cisly(adresy)
print(vysledek)