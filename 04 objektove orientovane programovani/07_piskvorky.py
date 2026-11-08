import random

class Board:
    """ hrací plocha: položení značky, kontrola volného pole, zjištění vítěze, __str__ pro vykreslení"""
    def __init__(self, n):
        self.n = n
        self.pole = []
        for i in range(self.n):
            self.pole.append([])
            for j in range(self.n):
                self.pole[i].append( " . ")

    def __str__(self):
        radek = ""
        for i in range(self.n):
            radek += "\n"
            for j in range(self.n):
                radek += self.pole[i][j]
            
        return radek

    def tah(self, x, y, hrac):
        if self.pole[x][y] != " . ":
            return False
        if hrac == 0:
            self.pole[x][y] = " x "
            return
        else:
            self.pole[x][y] = " o "
            return

    def vitez(self, hrac):
        if hrac == 0:
            znacka = " x "
        else:
            znacka = " o "  

        k = self.n
        smery = [(0, 1),(1, 0),(1, 1),(-1, 1)]

        for i in range(self.n):
            for j in range(self.n):
                if self.pole[i][j] != znacka:
                    continue

                for di, dj in smery:
                    rada = True
                    for posun in range(1, k):
                        ni = i + di * posun
                        nj = j + dj * posun

                        if not (0 <= ni < self.n and 0 <= nj < self.n) or self.pole[ni][nj] != znacka:
                            rada = False
                            break

                    if rada:
                        return True

        return False


class Player:
    """ společný předek hráčů s metodou choose_move(board)"""
    def __init__(self, hrac):
        self.hrac = hrac

    def choose_move(self, board, x, y):
        aktualni_tah = board.tah(x, y, self.hrac)
        if aktualni_tah == False:
            print("již zabrané nebo neplatné pole")
            self.choose_move(board)
        else:
            print(board)
        board.vitez(self.hrac)

class HumanPlayer(Player):
    """ tah načte od uživatele"""
    def __init__(self):
        znak = input("vyberte si znak (x/o):")
        if znak == "x":
            hrac = 0
        elif znak == "o":
            hrac = 1
        else:
            print("neplatný vstup")
        super().__init__(hrac)

    def choose_move(self, board):
        x = input("číslo řádku:")
        y = input("číslo sloupce:")
        return super().choose_move(board, x, y)

class RandomPlayer(Player):
    """ táhne náhodně na volné pole"""
    def __init__(self):
        znak = input("vyberte znak pro RandomPlayer (x/o):")
        if znak == "x":
            hrac = 0
        elif znak == "o":
            hrac = 1
        else:
            print("neplatný vstup")
        super().__init__(hrac)

    def choose_move(self, board):
        platny_tah = True
        while platny_tah:
            x = random.randrange(0, board.n - 1)
            y = random.randrange(0, board.n - 1)
            if board.tah(self, x, y, self.hrac) != False:
                platny_tah = True
        return super().choose_move(board, x, y)

class SmartPlayer:
    """ vyhraje, může-li. Jinak zablokuje soupeřovu výhru. Jinak táhne náhodně"""

class Game:
    """ střídá hráče, dokud někdo nevyhraje nebo není plocha plná"""
    def __init__(self):
        self.n = input("hrací pole:")
        hra = Board(n)
        self.hrac1 = HumanPlayer()
        self.hrac2 = RandomPlayer()
        self.pokracovat = True
        while self.vitez:
            print(hra)
        pass


ctyri = Board(4)
print(ctyri)
ctyri.značka(0,0,0)
ctyri.značka(0,1,0)
ctyri.značka(0,2,0)
ctyri.značka(1,1,0)
print(ctyri)
print(ctyri.vitez(0))