veta = input("Věta:").strip().lower()
cetnosti = {}
pismena = 0
for i in range(len(veta)):
    if veta[i].isalpha():
        if veta[i] in cetnosti:
            cetnosti[veta[i]] += 1
        else:
            cetnosti[veta[i]] = 1
            pismena += 1


cetnosti_list = list(cetnosti.items())
srovnane = sorted(cetnosti_list, key=lambda x: x[1], reverse=True)

for pismeno, pocet in srovnane:
    print(pismeno, ":", pocet)
print("Různých čísel: ", pismena)
