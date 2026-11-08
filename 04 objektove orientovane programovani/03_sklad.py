class Item:
    def __init__(self, name, quantity, unit_price):
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity

class Warehouse:
    def __init__(self):
        self.seznam = {}

    def add(self, name, quantity, unit_price):
        if name in self.seznam:
            self.seznam[name].quantity += quantity 
        else:
            self.seznam[name] = Item(name, quantity, unit_price)
        return

    def remove(self, name, quantity):
        if name in self.seznam:
            self.seznam[name].quantity -= quantity
            return
        else:
            return False

    def find(self, name):
        if name in self.seznam:
            return self.seznam[name]
        else:
            return

    def total_value(self):
        self.value = 0
        for i in self.seznam:
            self.value += self.seznam[i].unit_price * self.seznam[i].quantity
        return self.value

    def low_stock(self, limit):
        self.low = []
        for i in self.seznam:
            if self.seznam[i].quantity < limit:
                self.low.append(self.seznam[i])
        return self.low

    def report(self):
        for i in self.seznam.values(): 
            print(f"{i.name}; {i.unit_price} ,-; {i.quantity}")
        return

w = Warehouse()

w.add("kokos", 10, 109)
w.add("kokos", 5, 109)
w.add("pomeranč", 3, 399)
w.report()

print(w.find("pomeranč"))
print(w.find("ořech"))

print(w.total_value())

print(w.low_stock(10))

w.remove("kokos", 3)
w.report()