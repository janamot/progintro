n = int(input("celé číslo:"))
prvocislo = True

odmocnina = int(n**0.5)

for i in range(2, odmocnina +1):
    if n % i == 0:
        prvocislo = False
        break
    else:
        continue

print(f"číslo {n} je prvočíslo: {prvocislo}")

cisla = []
pocet = 0
for m in range(2,100):
    mprvocislo = True
    modmocnina = int(m**0.5)
    for i in range(2, modmocnina +1):
        if m % i == 0:
            mprvocislo = False
            break
        else:
            continue

    if mprvocislo:
        cisla.append(m)
        pocet += 1

print(cisla)
print(f"{pocet} prvočísel od 2 do 100")

soucinitel =  []
i = 2
p = 0
num = n
if prvocislo == False:
    while i <= odmocnina:
        if num % i == 0:
            soucinitel.append(i)
            num = num/i
            p += 1
        else:
            i += 1

soucin = ""
for l in range(p):
    if l < p-1:
        soucin += str(soucinitel[l])
        soucin += " * "
    else:
        soucin += str(soucinitel[l])

print(f"{n} = {soucin}")