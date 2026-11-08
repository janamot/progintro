import math
def rectangle(f, a, b, n):
    """obdelnikova metoda"""
    sirka = (b-a)/n
    area = 0
    for i in range(n):
        stred = a + (i + 0.5)*sirka
        area += sirka*f(stred)
    return area

def trapezoid(f, a, b, n):
    """lichoběžníková metoda"""
    sirka = (b-a)/n
    area = 0
    for i in range(n):
        x1 = a + i*sirka
        x2 = a + (i+1)*sirka
        area += ((f(x1) + f(x2)) * sirka)/2
    return area

def simpson(f, a, b, n):
    """Simpsonova metoda (n sudé)"""
    sirka = (b-a)/n
    area = 0
    for i in range(0, n, 2):
        x1 = a + i*sirka
        x2 = a + (i+1)*sirka
        x3 = a + (i+2)*sirka
        area += (sirka/3)*(f(x1)+4*f(x2)+f(x3))    
    return area

integral = 2
print("------ obdelník -------")
print(f" n=4: {rectangle(math.sin, 0, math.pi, 4) - integral}")
print(f" n=8: {rectangle(math.sin, 0, math.pi, 8) - integral}")
print(f"n=16: {rectangle(math.sin, 0, math.pi, 16) - integral}")
print(f"n=32: {rectangle(math.sin, 0, math.pi, 32) - integral}")
print(f"n=64: {rectangle(math.sin, 0, math.pi, 64) - integral}")    

print("------ lichoběžník -------")
print(f" n=4: {trapezoid(math.sin, 0, math.pi, 4) - integral}")
print(f" n=8: {trapezoid(math.sin, 0, math.pi, 8) - integral}")
print(f"n=16: {trapezoid(math.sin, 0, math.pi, 16) - integral}")
print(f"n=32: {trapezoid(math.sin, 0, math.pi, 32) - integral}")
print(f"n=64: {trapezoid(math.sin, 0, math.pi, 64) - integral}")

print("------ simpson -------")
print(f" n=4: {simpson(math.sin, 0, math.pi, 4) - integral}")
print(f" n=8: {simpson(math.sin, 0, math.pi, 8) - integral}")
print(f"n=16: {simpson(math.sin, 0, math.pi, 16) - integral}")
print(f"n=32: {simpson(math.sin, 0, math.pi, 32) - integral}")
print(f"n=64: {simpson(math.sin, 0, math.pi, 64) - integral}")
