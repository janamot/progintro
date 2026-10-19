sekundy = int(input("počet sekund: "))
hodiny = sekundy // 3600
minuty = (sekundy % 3600) // 60
vteriny = (sekundy % 3600) % 60
print(hodiny, ":", minuty, ":", vteriny)

#přidat nuly když <10
