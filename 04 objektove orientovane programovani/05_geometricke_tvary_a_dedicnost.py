class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        NotImplementedError

    def perimeter(self):
        NotImplementedError

    def describe(self):
        return f"Tvar: {self.name} | Obsah: {self.area():.2f} | Obvod: {self.perimeter():.2f}"

class Circle(Shape):
    def __init__(self, polomer):
        super().__init__("kruh")
        self.polomer = polomer

    def area(self):
        return 3.14 * self.polomer ** 2

    def perimeter(self):
        return 2 * 3.14 * self.polomer

class Rectangle(Shape):
    def __init__(self, a, b, name = "obdelník"):
        super().__init__(name)
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)

class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__("trojúhleník")
        self.a = a
        self.b = b
        self.c = c

        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            ValueError

    def area(self):
        s = (self.a + self.b + self.c)/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**(1/2)

    def perimeter(self):
        return self.a + self.b + self.c

class Square(Rectangle):
    def __init__(self, a):
        b = a
        super().__init__(a, b, name = "čtverec")

tvary = [Circle(5), Rectangle(4,5), Triangle(4,5,6), Square(5)]
total_area = 0
greatest_perimeter = ["", 0]

for i in tvary:
    print(i.describe())
    total_area += i.area()
    if i.perimeter() > greatest_perimeter[1]:
        greatest_perimeter[0] = i.name
        greatest_perimeter[1] = round(i.perimeter(),2)

print(round(total_area, 2))
print(greatest_perimeter)