class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height

    def is_square(self):
        if self.width == self.height:
            return True
        return False

    def scale(self, factor):
        self.height = factor * self.height
        self.width = factor * self.width

    def describe(self):
        self.description = ""
        if self.is_square():
            self.description += "Čtverec "
        else:
            self.description += "Obdelník "
        self.description += str(self.width) + " x " + str(self.height) + ", obsah " + str(self.area())
        return self.description



obdelnik1 = Rectangle(2, 4)
obdelnik2 = Rectangle(1, 5)
obdelnik3 = Rectangle(3, 3)

print(obdelnik1.describe())
print(obdelnik2.describe())
print(obdelnik3.describe())
