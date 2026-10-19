sekundy = int(input("počet sekund: "))

hodiny = sekundy // 3600
minuty = (sekundy % 3600) // 60
vteriny = (sekundy % 3600) % 60

if hodiny < 10:
    hodiny = "0" + str(hodiny)
if minuty < 10:
    minuty = "0" + str(minuty)
if vteriny < 10:
    vteriny = "0" + str(vteriny)

if sekundy >= 86400:
    dny = sekundy//86400
    hodiny = hodiny - dny * 24
    if dny < 10:
        dny = "0" + str(dny)
    print(f"{dny}:{hodiny}:{minuty}:{vteriny}")
else:
    print(f"{hodiny}:{minuty}:{vteriny}")

