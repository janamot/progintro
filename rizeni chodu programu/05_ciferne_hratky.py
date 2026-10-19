for i in range(100,1000):
    jednotky = i%10
    desitky = (i//10)%10
    stovky = (i//100)%10
    if jednotky**3 + desitky**3 + stovky**3 == i:
        print(i)

cislo = 38728663
soucet = [cislo]
l = 0
vypis = str(cislo)
while cislo > 9:
    cislo = str(cislo)
    l += 1
    soucet.append(0)
    for j in range(len(cislo)):
        soucet[l] = soucet[l] + int(cislo[j])
    cislo = soucet[l]

for m in range(1, l+1):
    vypis = vypis + " → " + str(soucet[m])
print(vypis)