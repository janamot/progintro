bit = 8
while bit <= 64:

    print(f"{bit:>2} bitů: 0 až {2**bit-1:<26,} {round(-(2**bit)/2):>27,} až {round((2**bit)/2-1):<26,}")
    bit = bit * 2
