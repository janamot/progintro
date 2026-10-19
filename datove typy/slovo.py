slovo = input("Slovo: ")

pocet = len(slovo)
prvni = slovo[0].strip().upper()
posledni = slovo[-1].strip().upper()
pozpatku = slovo[::-1]
if slovo.upper() == pozpatku.upper():
    palindrom = "ano"
else:
    palindrom = "ne"



print("Počet znaků: ", pocet)
print("První znak: ", prvni)
print("Poslední znak: ", posledni)
print("Velkými písmeny: ", slovo.strip().upper())
print("Pozpátku: ", pozpatku)
print("Palindrom: ", palindrom)