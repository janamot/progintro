from pathlib import Path
import os

def jpg_soubory(folder_path):
    image_files = []
    folder = Path(folder_path)
    files = soubory(folder)
    for file in files:
        suff = file.suffix.upper()
        if suff == ".JPG" or suff == ".JPEG":
            image_files.append(file)
    return image_files


def soubory(folder_path):
    files = []
    folder = Path(folder_path)
    for file in folder.iterdir():
        files.append(file)
    return files

def prejmenovani_souhlas(file, new_file):
    print()
    print("přejmenování souboru:")
    print()
    print(file.name, "-->", new_file.name)
    print()
    souhlas = input("přejmenovat? (A/N):")
    if souhlas.upper() == "A":
        return True
    else:
        return False

def prejmenovani(folder_path):
    images = jpg_soubory(folder_path)
    for i in range(len(images)):
        file = images[i]
        num = str(i + 1).zfill(3)
        nova_cesta = Path(folder_path) / f"photo_{num}.jpg"
        if nova_cesta.exists():
            print("soubor již existuje, přeskakuji")
            continue
        if prejmenovani_souhlas(file, nova_cesta):
            file.rename(nova_cesta)

def main(): 
    os.system('cls||clear')
    folder_path = input("složka:")
    prejmenovani(folder_path)

if __name__ == "__main__":
    main()