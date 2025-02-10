def liczenie_funkcji(stopien:[int],wspolczynniki:[float], wartość_zmiennej:[float]):
    wartość_funkcji = 0
    for i in range (0,stopien+1):
        dodawana_wartosc = (wartość_zmiennej**(stopien-i))*wspolczynniki[i]
        wartość_funkcji += dodawana_wartosc
    return wartość_funkcji
znaleziono = False
min = -500
x = min
max = 500.0
obszary = 10000
dlugosc = (max - min)/obszary
miejsca_zerowe = []
lista_zmianny_znaku = []
for i in range (0,obszary+1):
        funkcja_x = liczenie_funkcji(5, [3,2,-5,-8,9,2],x)
        funkcja_y = liczenie_funkcji(5, [3,2,-5,-8,9,2],(x+dlugosc))
        if (funkcja_x > 0 and funkcja_y < 0) or (funkcja_x < 0 and funkcja_y > 0):
            lista_zmianny_znaku.append([x,x+dlugosc])
            print(x)
            print(funkcja_x)
            print(funkcja_y)
        elif funkcja_x == 0 :
            print("Miejscem zerowym jest" + x)
            print(funkcja_x)
            miejsca_zerowe.append(x)
            znaleziono = True
        x += dlugosc
while znaleziono == False:
    x = min
    for i in range (0,obszary+1):
        funkcja_x = liczenie_funkcji(5, [3,2,-5,-8,9,2],x)
        funkcja_y = liczenie_funkcji(5, [3,2,-5,-8,9,2],(x+dlugosc))
        if (funkcja_x > 0 and funkcja_y < 0) or (funkcja_x < 0 and funkcja_y > 0):
            lista_zmianny_znaku.append([x,x+dlugosc])
            print(x)
            print(funkcja_x)
            print(funkcja_y)
        elif funkcja_x == 0 :
            print("Miejscem zerowym jest" + x)
            print(funkcja_x)
            miejsca_zerowe.append(x)
            znaleziono = True
        x += dlugosc
    znaleziono = True
