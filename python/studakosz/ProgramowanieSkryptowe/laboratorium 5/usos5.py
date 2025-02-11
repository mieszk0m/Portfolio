import random

class Student:
    def __init__(self,nazwisko:str, imie:str):
        self.nazwisko = nazwisko
        self.imie = imie
class Exercise:
    def __init__(self, name:str, max:int):
        self.name = name
        self.max = max
    def write_info(self):
        print(self.name  +  " ma limit maksymalnej liczby studentów wynoszący: " + str(self.max) )
class Lecture:
    def __init__(self, name:str, tryb:str):
        self.name = name
        if tryb == "zdalny" or tryb == "stacjonarny": 
            self.tryb = tryb
        else:
            print("Są tylko dwa możliwe tryby zajęć zdalny i stacjonarny")
    def write_info(self):
        print(self.name  +  " jest prowadzone w trybie  " + self.tryb )    
class Grade:
    def __init__(self, student:Student, subject, grade:str):
        self.subject = subject 
        if grade not in ["2.0", "3.0", "3.5", "4.0", "4.5", "5.0"]:
            print("Podano ocene z poza zakresu")
        else:
            self.grade = grade
class Usos:
    def __init__(self,subjects:list,  students:dict):
        self.subjects = list(subjects)
        self.students = students
    def wykaz_ocen_student_dla_studenta(self,nazwisko,imie):
        show = ""
        for studenci, przedmiot in self.students.items():
            if studenci.nazwisko == nazwisko and studenci.imie == imie:
                for przedmiocik, oceny in przedmiot.items():
                    show = ("            " + przedmiocik.name + " \n                            " )
                    for ocenka in oceny:
                        y = type(ocenka)
                        if y == str:
                            show = (show + ocenka + " ")
                        else:
                            oceny.remove(ocenka)
                    print(show)
        if show == "":
            print("Podano imie i nazwisko, którego nie ma w systemie")
    def dodaj_ocene(self, imie, nazwisko, subject, ocena, ostatnio_dodawany ):
        show = ""
        p = 0
        for studenci, przedmiot in self.students.items():
            if studenci.nazwisko == nazwisko and studenci.imie == imie:
                show = "kon"
                for przedmiocik, oceny in przedmiot.items():
                    if przedmiocik.name == subject:
                        p = 1
                        oceny.append(ocena)
        if show == "":
            print("Podano imie i nazwisko, którego nie ma w systemie")
        elif p == 0:
            print("Podano przedmiot którego nie ma w systemie")
    def usun_ocene(self, imie, nazwisko, subject, ocena) :
        show = ""
        p = 0
        o = 0
        for studenci, przedmiot in self.students.items():
            if studenci.nazwisko == nazwisko and studenci.imie == imie:
                show = "kon"
                for przedmiocik, oceny in przedmiot.items():
                    if przedmiocik.name == subject:
                        p = 1
                        if ocena in oceny:
                                o = 0
                                oceny.remove(ocena)
                    print(show)
        if show == "":
            print("Podano imie i nazwisko, którego nie ma w systemie")
        elif p == 0:
            print("Podano przedmiot którego nie ma w systemie")
        elif o == 0:
            print("Podano ocene którego nie ma w systemie")
        

Ziemowit_Kosakowski =Student("Kosakowski", "Ziemowit" )
Mieszko_Makowski = Student("Makowski", "Mieszko" ) 
Filip_Konieczny = Student("Konieczny", "Filip" )
matematyka = Lecture("Matematyka", "zdalny")
fizyka = Lecture("Fizyka", "stacjonarny")
historia = Exercise("Historia",4)
lista_przedmiotow = (historia,fizyka,matematyka)
ostatnio_dodawany = 4
lista_studentow = (Ziemowit_Kosakowski, Mieszko_Makowski, Filip_Konieczny)
lista = dict()
listka = dict()
for i in lista_studentow:
    for j in lista_przedmiotow:
        lista_ocen = []
        for k in range(3) :
            g = random.choice(["2.0", "3.0", "3.5", "4.0", "4.5", "5.0"])
            lista_ocen.append(g)
        listka[j] = lista_ocen
    lista[i] = listka
USOS = Usos(lista_przedmiotow, lista)
ostatnio_dodawany = 3
while True:
    try:
        x = input(">")
        if x == "subjects":
            lista = []
            for subject in USOS.subjects:
                lista.append(subject.name)
            print(lista)
        elif x == "students":
            lista = []
            for student in USOS.students:
                imie_nazwisko = (student.imie + "_"+ student.nazwisko)
                if imie_nazwisko not in lista:
                        imie_nazwisko = (student.imie + "_"+ student.nazwisko)
                        lista.append(imie_nazwisko)
            print(lista)
        elif x.startswith("student "):
            x = x.split(" ")
            imie = x[1]
            nazwisko = x[2]
            USOS.wykaz_ocen_student_dla_studenta(nazwisko, imie)
        elif x.startswith("add "):
            _, imie, nazwisko, przedmiot, ocena = x.split(" ")
            USOS.dodaj_ocene(imie, nazwisko, przedmiot, ocena, ostatnio_dodawany )
        elif x.startswith("remove "):
            _, index, przedmiot, ocena = x.split(" ")
            USOS.usun_ocene(imie, nazwisko, przedmiot, ocena)      
        elif x.startswith("add_subject "):
            subject_name = x.split(" ", 1)[1]
            x  = input("Jaka jest forma zajęć ")
            if x == "wykład":
                x  = input("Jaki jest tryb zajęć ")
                przedmiot = Lecture(subject_name,x)
                USOS.subjects.append(przedmiot)
            elif x == "ćwiczenia":
                x  = input("Jaki jest limit studentów: ")
                przedmiot = Exercise(subject_name,int(x))
                USOS.subjects.append(przedmiot)
            else:
                print("Nie ma takiej formy zajęć")
        elif x.startswith("write_info "):
            subject_name = x.split(" ", 1)[1]
            wypisz = 0
            for subject in USOS.subjects:
                if subject.name == subject_name:
                    subject.write_info()
                    wypisz = 1
            if wypisz == 0:
                print("Nie ma takiego przedmiotu jak: " + subject_name)
        else:
            print("Nie ma takiej komendy")
    except EOFError:
        print("\nZakończono działanie programu.")
        break