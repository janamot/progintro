cislo = int(input("číslo:"))
binarni = ""
jedna = 0
if cislo == 0:
    binarni = "0"
else:
    n = cislo

    while n >= 1:
        if n % 2 > 0:
            binarni = binarni + "1"
            jedna = jedna + 1
        else:
            binarni = binarni + "0"
        n = n//2


print("dvojkově:", binarni[::-1])
print("kontorla: ", bin(cislo))
print("počet bitů:", len(binarni))
print("počet jendiček:", jedna)
