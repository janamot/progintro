rok = int(input("rok:"))
prestupny = False

if rok % 4 == 0 and rok % 100 != 0 or rok % 400 == 0:
    prestupny = True

print(f"rok {rok} je přestupný: {prestupny}")
print("-" * 20)
roky = []
pocet = 0
for i in range(1890, 2031):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        roky.append(i)
        pocet += 1
p = pocet
while p > 9:
    deset = []
    for j in range(10):
        deset.append(roky[0])
        roky.remove(roky[0])
    p = p - 10
    print(deset)
print(roky)
print(f"{pocet} přestupných let")