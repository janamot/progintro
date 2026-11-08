import math

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Jmenovatel nesmí být 0")
        if b < 0:
            a = -a
            b = -b
        delitel = math.gcd(a,b)
        self.a = a // delitel
        self.b = b // delitel

    def __str__(self):
        return f"{self.a} / {self.b}"

    def __add__(self, other):
        return Fraction(self.a * other.b + other.a * self.b, self.b * other.b)

    def __sub__(self, other):
        return Fraction(self.a * other.b - other.a * self.b, self.b * other.b)

    def __mul__(self, other):
        return Fraction(self.a * other.a, self.b * other.b)

    def __truediv__(self, other):
        return Fraction(self.a * other.b, self.b * other.a)

    def __eq__(self, value):
        if self.a / self.b == value:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.a / self.b < other.a / other.b:
            return True
        else:
            return False

    def to_float(self):
        return float(self.a / self.b) 
    

print(Fraction(1, 2) + Fraction(1, 3))    # 5/6
print(Fraction(2, -4))                    # -1/2
print(Fraction(1, 3) < Fraction(1, 2))    # True
