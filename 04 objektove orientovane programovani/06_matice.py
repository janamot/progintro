import copy

class Matrix:
    def __init__(self, matice):
        
        necele = False
        for i in range(len(matice)-1):
            if len(matice[i]) != len(matice[i+1]):
                necele = True

        if necele:
            print("špatně zadaná matice")
            return

        self.matice = matice
        

    def shape(self):
        self.radky = len(self.matice)
        self.sloupce = len(self.matice[0])
        return f"{self.radky} x {self.sloupce}"

    def __str__(self):
        self.shape()
        self.sirka = 1
        self.matice_print = ""
        for i in range(self.radky):
            for j in range(self.sloupce):
                if len(str(self.matice[i][j])) > self.sirka:
                    self.sirka = len(str(self.matice[i][j]))
        for i in range(self.radky):
            for j in range(self.sloupce):
                mezery = self.sirka - len(str(self.matice[i][j]))
                self.matice_print += " "*mezery + str(self.matice[i][j]) + "  "
            self.matice_print += "\n"
        return self.matice_print

    def transpose(self):
        self.shape()
        transpozice = []
        for i in range(self.sloupce):
            transpozice.append([])
            for j in range(self.radky):
                transpozice[i].append(self.matice[j][i])
        return Matrix(transpozice)

    def __add__(self, other):
        if self.shape() != other.shape():
            raise ValueError("Cannot add matrixes")
        self.soucet = []
        for i in range(self.radky):
            self.soucet.append([])
            for j in range(self.sloupce):
                self.soucet[i].append(self.matice[i][j] + other.matice[i][j])
        return Matrix(self.soucet)

    def __mul__(self, other):
        self.shape()
        other.shape()
        self.soucin = []
        if self.sloupce != other.radky:
             raise ValueError("Cannot multiplicate matrixes")
        for i in range(self.radky):
            self.soucin.append([])
            for j in range(other.sloupce):
                soucet = 0
                for k in range(self.sloupce):
                    soucet += self.matice[i][k] * other.matice[k][j]
                self.soucin[i].append(soucet)
        return Matrix(self.soucin)
    @staticmethod
    def identity(n):
        jednotkova = []
        for i in range(n):
            jednotkova.append([])
            for j in range(n):
                if i == j:
                    jednotkova[i].append(1)
                else:
                    jednotkova[i].append(0)
        return Matrix(jednotkova)

        

a_matice = Matrix([[1,1,0], [2,22,2]])
b_matice = Matrix([[2,22,2], [1,1,0]])
c_matice = Matrix([[0], [1], [1]])
print(c_matice)
print(a_matice.transpose())
print(a_matice + b_matice)
print(a_matice * c_matice)
print(Matrix.identity(4))


