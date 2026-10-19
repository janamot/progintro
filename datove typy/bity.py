bit = 8
while bit <= 64:
    print(bit, "bitů:", bit*0, "až", 2**bit-1, ",", round(-(2**bit)/2), "až", round((2**bit)/2-1))
    bit = bit * 2