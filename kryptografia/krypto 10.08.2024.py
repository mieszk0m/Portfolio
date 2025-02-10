#zad1
def prime_root(n):
    if n % 2 != 0:
        lista_elementów = []
        for i in range (1,n):
            lista_elementów.append(i)
        k = 0
        znaleziono = False
        print(lista_elementów)
        while (k != n) and (znaleziono == False):
            z = 0
            print(k)
            skonczono = False
            lista = []
            while (z != n) and (skonczono == False):
                print(z)
                lista.append(pow(k,z,n))
                z += 1
                if pow(k,0,n) == pow(k,z,n):
                    skonczono = True
            lista.sort() 
            print(lista)
            if lista == lista_elementów:
                znaleziono = True
                p = k
                print("Najmniejszym pierwiastkiem pierwotnym jest " + str(p))
            k += 1           
    else: 
        print("Nie ma pierwiastka pierwotnego")
prime_root(7)
prime_root(15)
prime_root(2)

#zad2
class Zn:
    def __init__(self, value, N):
        #"""Inicjalizacja obiektu klasy Zn."""
        self.N = N  # Modulo N
        self.value = value % N  # Element w pierścieniu Zn(N)
    
    def __add__(self, other):
        #"""Przeładowanie operatora dodawania."""
        if isinstance(other, Zn):  # Jeśli dodajemy obiekt Zn
            return Zn((self.value + other.value) % self.N, self.N)
        elif isinstance(other, int):  # Jeśli dodajemy liczbę całkowitą
            return Zn((self.value + other) % self.N, self.N)
        return NotImplemented

    def __sub__(self, other):
        #"""Przeładowanie operatora odejmowania."""
        if isinstance(other, Zn):
            return Zn((self.value - other.value) % self.N, self.N)
        elif isinstance(other, int):
            return Zn((self.value - other) % self.N, self.N)
        return NotImplemented

    def __mul__(self, other):
        #"""Przeładowanie operatora mnożenia."""
        if isinstance(other, Zn):
            return Zn((self.value * other.value) % self.N, self.N)
        elif isinstance(other, int):
            return Zn((self.value * other) % self.N, self.N)
        return NotImplemented

    def __pow__(self, exponent):
        #"""Przeładowanie operatora potęgowania."""
        if isinstance(exponent, int):  # Potęgowanie liczby całkowitej
            return Zn(pow(self.value, exponent, self.N), self.N)
        return NotImplemented

    def __repr__(self):
        #"""Reprezentacja obiektu jako string."""
        return f"Zn({self.value}, {self.N})"
    

