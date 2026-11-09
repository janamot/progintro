from datetime import datetime
import os

def add(path, text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(path, "a", encoding="utf-8") as file:
        file.write(timestamp)
        file.write(" : ")
        file.write(text)
        file.write("\n")

def list(path):
    with open(path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            print(line_number,line)

def search(path, text):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            if text in line:
                print(line)

def main():
    os.system('cls||clear')
    path = "05 prace se soubory\jornal.txt"
    add(path, "ss")
    list(path)
    search(path, "j, 2")
    add(path,"blabla")

if __name__ == "__main__":
    main()
