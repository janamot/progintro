def max_of_three(a,b,c):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max

def format_price(cena, currency="Kč"):
    return f"{cena:.2f} {currency}"


print(max_of_three(3, 9, 5))             # 9
print(max_of_three(-1, -8, -3))          # -1
print(format_price(1800))                # 1800.00 Kč
print(format_price(72.5, currency="€"))  # 72.50 €