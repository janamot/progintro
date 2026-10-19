text = input("text: ")
byty = 0
for i in range(len(text)):
    #znak = text[i]
    byte = len(text[i].encode("utf-8"))
    print(text[i], f"U+{ord(text[i]):04X}", byte, "B")
    byty = byty + byte

print("Znaků: ", len(text), ", bajtů:", byty)
