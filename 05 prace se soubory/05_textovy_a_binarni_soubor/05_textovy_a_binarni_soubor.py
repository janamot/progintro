from pathlib import Path
import os

def cela(path):
    with open(path, "w", encoding="utf-8") as file:
        for i in range(0,65536):
            file.write(f"{i}")
            if i < 65535:
                file.write("\n")
        
def bajty(path):
    with open(path, "wb") as file:
        for i in range(0,65536):
            cislo = i.to_bytes(2)
            file.write(cislo)

def velikost(path):
    path_velikost = Path(path)
    return path_velikost.stat().st_size

def nacteni_cela(path):
    with open(path, "r", encoding="utf-8") as file:
        for i, line in enumerate(file, start=0): 
            cleaned = line.strip("\n")
            if str(i) != str(cleaned):
                return False
    return True

def nacteni_bajty(path):
    with open(path, "rb") as file:
        pocet = velikost(path)//2
        for i in range(0, pocet): 
            cislo = int.from_bytes(file.read(2), byteorder='big', signed=False)
            if i != cislo:
                return False
    return True

def main():
    os.system('cls||clear')
    path_cele = r"05 prace se soubory\05_textovy_a_binarni_soubor\cela.txt"
    path_bajty = r"05 prace se soubory\05_textovy_a_binarni_soubor\bajty.bytes"
    cela(path_cele)
    bajty(path_bajty)
    print("velikost celých: ", velikost(path_cele))
    print("velikost bajtů:  ", velikost(path_bajty))
    print(nacteni_cela(path_cele))
    print(nacteni_bajty(path_bajty))

if __name__ == "__main__":
    main()