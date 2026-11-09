import pathlib as Path

def text_statistics(path):
    clean_lines = 0
    lines = 0
    words = 0
    char = 0
    nejdelsi = 0
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            lines += 1
            cleaned = line.strip("\n")
            if cleaned == "":
                clean_lines += 1
                continue
            word_list = line.split()
            words += len(word_list)
            characters = 0
            characters += sum(len(word) for word in word_list)
            char += characters
            if characters > nejdelsi:
                nejdelsi = characters

            
    nonclean_lines = lines - clean_lines
    return {"všechny řádky":lines, "neprázdné řádky":nonclean_lines,"slova":words, "znaky":char, "nejdelší": nejdelsi}

def main():
    path = input("cesta k souboru:")
    
    try:
        print(text_statistics(path))
    except FileNotFoundError:
        print("soubor nenalezen")

if __name__ == "__main__":
    main()