delka = float(input("Délka v mm:"))
cm = round(delka / 10, 3)
m = round(delka / 1000, 3)
palce = round(delka / 25.4, 3)

print(delka, "mm = ", cm, "cm = ", m, "m = ", palce, "in")

#vypsat 3 desetinná místa