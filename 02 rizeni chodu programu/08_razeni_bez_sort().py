import random
srovnane = list(range(1,101))
opacne = list(range(100,0,-1))
nahodny = [random.randint(1,101) for j in range(100)]
cislo = nahodny

porovnani = 0
prohozeni = 0
while True:
    i = 0
    konec = 0
    for i in range(len(cislo)-1):
        a = cislo[i]
        b = cislo[i+1]
        porovnani += 1
        if a>b:
            cislo[i], cislo[i+1] = cislo[i+1], cislo[i]
            konec += 1
            prohozeni += 1
    if konec <= 0:
        break

print(cislo)
print("porovnaní:", porovnani)
print("prohození:", prohozeni)