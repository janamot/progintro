velikost = 10
pole = [["." for _ in range(velikost)] for _ in range(velikost)]
pole[0][1] = "#"
pole[1][2] = "#"
pole[2][0] = "#"
pole[2][1] = "#"
pole[2][2] = "#"
for radek in pole:
    print(" ".join(radek))
print()
okolo = [(1,-1),(1,0),(1,1),(0,-1),(0,1),(-1,-1),(-1,0),(-1,1)]

for _ in range(10):
    generace = [["." for _ in range(velikost)] for _ in range(velikost)]
    for r in range(len(pole)):
        for s in range(len(pole)):

            sousedi = 0
            for dr, ds in okolo:
                if 0 <= r+dr < 10 and 0 <= s+ds < 10:
                    if pole[r+dr][s+ds] == "#":
                        sousedi += 1

            if pole[r][s] == "." and sousedi == 3:
                generace[r][s] = "#"
            elif pole[r][s] == "#" and (sousedi == 2 or sousedi == 3):
                generace[r][s] = "#"
            else:
                generace[r][s] = "."

    pole = generace
    for radek in generace:
        print(" ".join(radek))
    print()