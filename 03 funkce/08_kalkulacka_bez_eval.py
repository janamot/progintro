def tokenize(text):
    tokeny = []
    i = 0
    operatory = ["*", "/", "+", "-", "(", ")"]
    while i < len(text):
        if text[i] == " ":
            i += 1
        elif text[i] in operatory:
            tokeny.append(text[i])
            i += 1
        else:
            j = i
            while j < len(text):
                if text[j] == " " or text[j] in operatory:
                    break
                else:
                    j += 1
            tokeny.append(text[i:j])
            i = j
    return tokeny

def evaluate(text):
    tokeny = tokenize(text)     # Nejdříve text rozsekáme na jednotlivé tokeny
    idx = 0                     # Ukazatel (index) na aktuálně zpracovávaný token

    # 1. ČINITEL: Zpracovává závorky, unární mínus a samotná čísla (nejvyšší priorita)
    def cinitel():
        nonlocal idx            # Říkáme, že budeme upravovat proměnnou idx z nadřazené funkce
        if idx >= len(tokeny):
            return 0
        token = tokeny[idx]     # Vezmeme aktuální token
        idx += 1                # Posuneme ukazatel na další v pořadí
        
        if token == '(':        # Pokud narazíme na otevírací závorku...
            val = vyraz()  # ...rekurzivně spočítáme celý vnitřek závorky jako nový výraz
            if idx < len(tokeny) and tokeny[idx] == ')':
                idx += 1        # Přeskočíme uzavírací závorku ')'
            return val
        elif token == '-':      # Pokud narazíme na záporné znaménko (unární mínus)...
            return -cinitel() # ...vynásobíme následující činitel zápornou hodnotou
        else:                   # Jinak to musí být obyčejné číslo
            return float(token) # Převedeme text na desetinné číslo a vrátíme ho

    # 2. ČLEN: Zpracovává násobení a dělení (střední priorita)
    def clen():
        nonlocal idx
        val = cinitel()    # Získáme první činitel
        # Dokud je dalším tokenem * nebo /, pokračujeme v násobení/dělení
        while idx < len(tokeny) and tokeny[idx] in ('*', '/'):
            op = tokeny[idx]    # Uložíme si operátor (* nebo /)
            idx += 1            # Posuneme ukazatel
            next_val = cinitel() # Získáme další činitel v pořadí
            if op == '*':
                val *= next_val # Provedeme násobení
            elif op == '/':
                val /= next_val # Provedeme dělení
        return val              # Vrátíme mezivýsledek členu

    # 3. VÝRAZ: Zpracovává sčítání a odčítání (nejnižší priorita)
    def vyraz():
        nonlocal idx
        val = clen()      # Získáme první člen (který má již vyřešené násobení/dělení)
        # Dokud je dalším tokenem + nebo -, pokračujeme ve sčítání/odčítání
        while idx < len(tokeny) and tokeny[idx] in ('+', '-'):
            op = tokeny[idx]    # Uložíme si operátor (+ nebo -)
            idx += 1            # Posuneme ukazatel
            next_val = clen() # Získáme další člen
            if op == '+':
                val += next_val # Provedeme sčítání
            elif op == '-':
                val -= next_val # Provedeme odčítání
        return val              # Vrátíme finální spočítanou hodnotu

    return vyraz()         # Spustíme vyhodnocení od nejnižší priority (výrazu)



print(evaluate("2 * (3 + 4) - 10 / 5"))   # 12.0
print(evaluate("-(1 + 2) * 3"))  