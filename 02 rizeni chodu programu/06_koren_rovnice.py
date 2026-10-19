dolni = float(2) 
horni = float(3)
presnost = 10**(-6)
iterace = 0
while horni-dolni > presnost:
    polovina = float((horni + dolni)/2)
    iterace += 1
    dolni_fce = float(dolni**3 - 2*dolni -5)
    polovina_fce = float(polovina**3 - 2*polovina -5)
    horni_fce = float(horni**3 - 2*horni -5)
    if dolni_fce <= 0 and polovina_fce >= 0:
        horni = polovina
    elif polovina_fce <= 0 and horni_fce >= 0:
        dolni = polovina

print(iterace, ":", polovina)