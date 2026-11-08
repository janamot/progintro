import pandas as pd

def normalize(birth_number):
    birth_number = birth_number.replace("/", "")
    birth_number = birth_number.replace(" ", "")
    if len(birth_number) == 10:
        return birth_number
    else:
        return
# odstraní lomítko a mezery, vrátí řetězec 10 číslic, nebo None, pokud vstup nemá správný tvar

def is_valid(birth_number):
    soucet = 0
    birth_number = normalize(birth_number)
    if int(birth_number) % 11 == 0 and (0 < int(birth_number[2:4]) < 13 or 50 < int(birth_number[2:4]) < 63):
        return "platný"
    else:
        return "neplatný"
# ověří tvar, dělitelnost 11 a platnost měsíce

def gender(birth_number):
    birth_number = normalize(birth_number)
    if 5 <= int(birth_number[2]) < 7:
        return "žena"
    elif 0 <= int(birth_number[2]) < 3:
        return "muž"
    else:
        return
# vrátí "muž" nebo "žena"

def birth_date(birth_number):
    birth_number = normalize(birth_number)

    if int(birth_number[:2]) >= 54:
        year = "19" + birth_number[:2]
    else:
        year = "20" + birth_number[:2]

    if gender(birth_number) == "muž":
        month = birth_number[2:4]
    else:
        month = str(int(birth_number[2:4]) - 50)
        month.zfill(2)


    day = birth_number[4:6]

    date = day + "." + month + "." + year
    return date
# vrátí datum narození jako řetězec.

rc1 = "736028/5163"
rc2 = "990101/1230"
rc3 = "736028/5164"
print(f"{rc1} --> {is_valid(rc1)}, {gender(rc1)}, {birth_date(rc1)}" )
print(f"{rc2} --> {is_valid(rc2)}, {gender(rc2)}, {birth_date(rc2)}" )
print(f"{rc3} --> {is_valid(rc3)}, {gender(rc3)}, {birth_date(rc3)}" )