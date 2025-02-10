class Zn:
    def __init__(self,liczba:int,mod:int):
        self.liczba = liczba
        self.mod = mod
    def __add__(self, other):
        if type(other) == int:
            self.liczba = self.liczba + other
        elif type(other) == Zn:
            print(self.liczba)
            print(other.liczba)
            self.liczba = self.liczba + other.liczba 
        while self.liczba >= self.mod:
            self.liczba -= self.mod
        return self.liczba
    def __radd__(self, other):
        return self.__add__(other)
    def __sub__(self, other):
        if type(other) == int:
            self.liczba = self.liczba - other
        elif type(other) == Zn:
            self.liczba = self.liczba - other.liczba 
        while self.liczba <= self.mod:
            self.liczba += self.mod
        return self
    def __rsub__(self, other):
        return self.__sub__(other)
    def __mul__(self, other):
        if type(other) == int:
            self.liczba = self.liczba * other
        elif type(other) == Zn:
            self.liczba = self.liczba * other.liczba 
        while self.liczba >= self.mod:
            self.liczba -= self.mod
        return self
    def __pow__(self, other):
        if type(other) == int:
            self.liczba = self.liczba ** other
        elif type(other) == Zn:
            self.liczba = self.liczba ** other.liczba 
        while self.liczba >= self.mod:
            self.liczba -= self.mod
        return self
    def __repr__(self):
        while self.liczba >= self.mod:
            self.liczba -= self.mod
        return str(self.liczba)
x=Zn(2,7)
y=Zn(10,7)
z=Zn(14,7)
print(x,y,z)
print(x+z, x*y, x**y,6+x,x+6)