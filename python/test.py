def wczytywanie_danych_z_pliku(nazwa_pliku: str):
    dane = []
    with open(nazwa_pliku, "r") as file:
        for line in file:
            line = line.strip()
            parts = line.split(' | ')
            studentci = []
            grades = []
            for part in parts[1:]:
                dane_studenta = part.split(' : ')
                studentci.append(dane_studenta[0])
                oceny = (dane_studenta[1]).split(' , ')
                grades.append(oceny)
            dane.append([parts[0], studentci, grades])
        return dane


def wyswietlenie_ocen(tablica_ocen: list):
    print("""----------+----------+-------+ 
Przedmiot | Studenci | Oceny |
----------+----------+-------+""")
    for przedmiot in tablica_ocen:
        pierwsza_linia = True
        indeks = 1
        for uczen, oceny in zip(przedmiot[1], przedmiot[2]):
            przedmiot_str = przedmiot[0] if pierwsza_linia else ""
            przedmiot_str = przedmiot_str.ljust(16)
            uczen_str = uczen.ljust(16)
            indeks_str = str(indeks)
            uczen_str = (indeks_str + ". " + uczen_str)
            oceny_str = " ".join(oceny)
            indeks += 1
            print(f"{przedmiot_str}{uczen_str}{oceny_str}")
            pierwsza_linia = False


def sprowadzenie_formatu_komendy(x: str, znak: str):
    if (")" in x) and ("|" in x) and (("-=" in x) or ("+=" in x)):
        wyjsciowe = dekonstrukcja_komendy(x, znak)
        return wyjsciowe
    else:
        print("Zły format komendy")
        print("""Format komendy dla dodawania: Nazwa_studenta1+=Przedmiot1(oceny)|Przedmiot2(oceny)""")
        print("""Format komendy dla odejmowania: Nazwa_studenta1+=Przedmiot1(oceny)|Przedmiot2(oceny)""")


def dekonstrukcja_komendy(x: str, znak: str):
    wyjsciowe = []
    if ") " in x:
        uczniowie = x.split(") ")

    else:
        uczniowie = [x]
    for uczen in uczniowie:
        uczen = uczen.replace(")", "")
        student = []
        parts = uczen.split(znak)
        student.append(parts[0])
        parts = parts[1].split("|")
        przedmioty = []
        oceny = []
        for part in parts:
            czesci = part.split("(")
            przedmioty.append(czesci[0])
            grades = czesci[1].split(", ")
            for grade in grades:
                if grade not in ["2.0", "3.0", "3.5", "4.0", "4.5", "5.0"]:
                    print("Podano ocene z poza zakresu")
                    return
            oceny.append(grades)
        student.append(przedmioty)
        student.append(oceny)
        wyjsciowe.append(student)
        print(wyjsciowe)
    return wyjsciowe


def zmiana(tablica_ocen: list, x: list, znak: str):
    print(x)
    lista_przedmiotow = []
    lista_uczniow = []
    for przedmiot in tablica_ocen:
        lista_przedmiotow.append(przedmiot[0])
        for uczen in przedmiot[1]:
            lista_uczniow.append(uczen)
    for uczen in x:
        if uczen[0] not in lista_uczniow:
            print("Nie ma takiego studenta jak " + uczen[0])
            return
        for indeks, subject in enumerate(uczen[1]):
            if subject not in lista_przedmiotow:
                print("Nie ma takiego przedmiotu jak " + subject)
                return
            for i, subject_szukany in enumerate(tablica_ocen):
                if subject == subject_szukany[0]:
                    for j, student in enumerate(subject_szukany[1]):
                        if student == uczen[0]:
                            if znak == "+=":
                                for ocenka in uczen[2][indeks]:
                                    tablica_ocen[i][2][j].append(ocenka)
                            else:
                                for ocenka in uczen[2][indeks]:
                                    if ocenka in tablica_ocen[i][2][j]:
                                        tablica_ocen[i][2][j].remove(ocenka)
                                    else:
                                        print("Uczeń " + uczen[
                                            0] + " nie ma takiej oceny z przedmiotu " + subject + " jak podane przez Ciebie " + ocenka)
    return tablica_ocen