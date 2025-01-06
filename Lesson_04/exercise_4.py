seznam_slov = ["jablko", "pomeranč", "banán", "kiwi", "hruška"]

#delky_slov = {ovoce: len(ovoce) for ovoce in seznam_slov}
delky_slov = {}
for ovoce in seznam_slov:
    delky_slov[ovoce] = len(ovoce)

print(delky_slov)