import sys 
from funkcje_usos import *

def dodaj_oceny(dane, komenda):
    # Dodaje oceny do danych na podstawie przekazanej komendy
    pass

def usun_oceny(dane, komenda):
    # Usuwa oceny z danych na podstawie przekazanej komendy
    pass

def obsluga_komendy(dane, komenda):
    if komenda == "grades":

        wyswietlanie_usos()
    elif "+=" in komenda:
        dodaj_oceny(dane, komenda)
    elif "-=" in komenda:
        usun_oceny(dane, komenda)
    else:
        print("Nieznana komenda")

def main(nazwa_pliku):
    lista_przedmiotow, lista_studentow, lista_ocen = pobieranie_bazy_usosa('c:/Desktop/ProgramowanieSkryptowe/USOSY/bazausos.txt')

    while True:
        try:
            komenda = input("> ")
            if komenda:
                obsluga_komendy(dane, komenda)
        except EOFError:
            break

    print("Zakończenie programu")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Użycie: python skrypt.py nazwa_pliku")
        sys.exit(1)

    main(sys.argv[1])

#lista_przedmiotow, lista_studentow, lista_ocen = pobieranie_bazy_usosa('c:/Desktop/ProgramowanieSkryptowe/USOSY/bazausos.txt')
#wyswietlanie_usos(listaa,listab,listac)
