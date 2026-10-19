delka = float(input("Délka v mm:"))
cm = round(delka / 10, 3)
m = round(delka / 1000, 3)
palce = round(delka / 25.4, 3)


print(f"{delka:.3f} mm = {cm:.3f} cm = {m:.3f} m = {palce:.3f} in")
