diameter = [25.01, 24.97, 25.06, 25.00, 24.94, 25.03, 25.05, 24.95, 25.10, 24.99]
tolerance = 0.05
prumer = 25.00
zmetci = 0

for i in range(len(diameter)):
    if prumer - tolerance <= diameter[i] <= prumer + tolerance:
        velikost = "OK"
    elif diameter[i] <= prumer - tolerance:
        velikost = "MALÝ"
        zmetci += 1
    else:
        velikost = "VELKÝ"
        zmetci += 1
    print(f"{i+1}: {diameter[i]} mm  {velikost}")

print(f"Zmetků: {zmetci} z {len(diameter)} ({zmetci/len(diameter)*100}%)")