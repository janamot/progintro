import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def length(self):
        return ((self.x)**2 + (self.y)**2)**(1/2)

    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def scale(self, k):
        return Vector2D(k * self.x, k * self.y)

    def dot(self, other):
        return (self.x * other.x + self.y * other.y)

    def angle_to(self, other):
        return math.degrees(math.acos(self.dot(other)/(self.length()*other.length())))

u = Vector2D(3, 4)
v = Vector2D(1, 0)
print(u, u.length())                    # (3, 4) 5.0
print(u.add(v))                         # (4, 4)
print(v.angle_to(Vector2D(0, 1)))       # 90.0