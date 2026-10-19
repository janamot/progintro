import math
import sys

deset = float(0)
for i in range(0,10):
    deset = deset + 0.1

print(deset)
print("deset == 1:", deset == 1)
print("math.isclose():", math.isclose(deset, 1))
#číslo 0.1 nelze ve dvojkové soustavě reprezentovat přesně 
#při sčítání vzniká drobná zaokrouhlovací chyba
#obě čísla v rámci povolené tolerance prakticky rovna --> math.isclose() = True

print("-------------")

eps = 1.0
while 1.0 + eps != 1.0:
    eps = eps/2.0

print("nejmenší eps:", eps)
print("strojové:", sys.float_info.epsilon)
print("rovnají se:", eps == sys.float_info.epsilon)
#Strojové epsilon = nejmenší kladný přírůstek, o který se musí hodnota 1.0 zvětšit, aby počítač dokázal nový výsledek rozlišit od původní jedničky

print("--------------")

n = 0
while float(2**n + 1) != float(2**n):
    n += 1
    print(n, " : ", float(2**n))
    print("+1  : ", float(2**n+1))

print()
print(n, " : ", float(2**n))
print("+1  : ", float(2**n+1))
print(n, "-int : ", 2**n)
print("+1 -int : ", 2**n+1)
#n = vzdálenost mezi dvěma po sobě jdoucími čísly typu float větší než 1, takže počítač přičtení jedničky zaokrouhlí a ztratí


