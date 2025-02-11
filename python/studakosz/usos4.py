class Usos:
    def __init__(self, subjects:list[str], grades:tuple[int,int,int,int]):
        self.subjects = subjects
        self.grades = grades
class Student:
    def __init__(self, id:int, nazwisko:str, imie:str):
        self.id = id
        self.nazwisko = nazwisko
        self.imie = imie
class Grade:
     def __init__(self, student:Student, subject: str, grade: int):
        self.Student = student
        self.subject = subject 
        self.grade = grade
USOS = Usos(["matematyka", "geografia", "fizyka"],(2,3,4,5))
students_list = []
grades_list = []
aktual_id = 1

def show_usos(lista_studentow:list[Student], y:Usos, lista_ocen: list[Grade]):
    if lista_studentow == []:
        print("Nie dodano jeszcze żadnego studenta")
    for studencik in lista_studentow:
        print(studencik.id,"  ",studencik.imie,"   ",studencik.nazwisko)
        for przedmiot in y.subjects:
            print ("---" + przedmiot + "---")
            for ocena in lista_ocen:
                if ocena.subject == przedmiot:
                    if ocena.student == studencik: # type: ignore
                        print(ocena.grade)
def dodawanie_oceny(lista_studentow:list[Student], y:Usos,lista_ocen: list[Grade],aktual:int):
    print("Oto lista studentów:")
    for studencik in lista_studentow:
        print(studencik.id,"-", studencik.imie,' ',studencik.nazwisko)
    x = int(input("Podaj ID studenta, któremu chcesz dodać ocenę"))
    z = 0
    for studencik in lista_studentow:
        if x == studencik.id:
            z = 1
            numer_przedmiotu = 0
            print("Oto lista przedmiotów")
            for przedmiot in y.subjects:
                numer_przedmiotu += 1 
                print (numer_przedmiotu," - ",przedmiot)
            przedmiot_oceny= int(input("Z którego przedmiotu chcesz dodać ocenę"))
            while (0 < przedmiot_oceny) and (przedmiot_oceny < (len(y.subjects) + 1)):
                print("Nie ma takiego przedmiotu")
                print("Oto lista przedmiotów")
                numer_przedmiotu = 0
                for przedmiot in y.subjects:
                    numer_przedmiotu += 1 
                    print (numer_przedmiotu," - ",przedmiot)
                przedmiot_oceny= int(input("Z którego przedmiotu chcesz dodać ocenę"))
            numer_przedmiotu = 0
            nazwa_przedmiotu = ""
            for przedmiot in y.subjects:
                numer_przedmiotu += 1 
                if numer_przedmiotu == przedmiot_oceny:
                    nazwa_przedmiotu = przedmiot
            nowa_ocena = int(input("Jaką ocenę chcesz dodać"))
            while (1 < nowa_ocena) and (nowa_ocena < 6):
                print("Nie ma takiej oceny, możliwe oceny do wystawienia to 2,3,4 i 5")
                nowa_ocena = int(input("Jaką ocenę chcesz dodać"))
            for studencik in lista_studentow:
                if studencik.id == x:
                    nowy_student = Grade(studencik,nazwa_przedmiotu,nowa_ocena)
                    lista_ocen.append(nowy_student)
        if x == studencik.id:
            z = 1
    if z != 1:
        aktual = x + 1
        print("Nie ma studenta z takim id, dodano zatem studenta o takim id")
        a = str(input("Podaj Imię tego studenta."))
        b = str(input("Podaj Nazwisko tego studenta."))
        nowy_student = Student(x,b,a)
        lista_studentow.append(nowy_student)
        print("Student " + a + b + " został dodany")
def usun_ocene(lista_studentow:list[Student], y:Usos,lista_ocen: list[Grade]): 
    z = 0
    if lista_ocen != []:
        while z!=0: 
            print("Oto lista studentów, ")
            for studencik in lista_studentow:
                print(studencik.id,"-", studencik.imie,' ',studencik.nazwisko)
            x = int(input("Podaj ID studenta, któremu chcesz usunąć ocenę"))
            for studencik in lista_studentow:
                if x == studencik.id:
                    z = 1
            if z != 1:
                print("Nie ma studentem z takim id, spróbuj jeszcze raz")
    print("Nie ma dodanej jeszce żadnej oceny")
def show_id(lista_studentow:list[Student], y:Usos,lista_ocen: list[Grade]):
    x = int(input("Podaj ID studenta, którego chcesz wyświetlić oceny"))   
    for studencik in lista_studentow:
        if studencik.id == x:
            print(studencik.id,"  ",studencik.imie,"   ",studencik.nazwisko)
            for przedmiot in y.subjects:
                print ("---" + przedmiot + "---")
                for ocena in lista_ocen:
                    if ocena.subject == przedmiot:
                        if ocena.student == studencik: # type: ignore
                            print(ocena.grade)
def dodaj_przedmiot(lista_przedmiotów: list[str]):
    x = str(input("Podaj nazwę nowego przedmiotu?"))
    lista_przedmiotów.append(x)
    print("Przedmiot " + x + " został dodany")
def dodaj_studenta(lista_studentów:list[Student],aktual: int):
    a = str(input("Podaj Imię studenta."))
    b = str(input("Podaj Nazwisko studenta."))
    nowy_student = Student(aktual,b,a)
    print(aktual)
    aktual = aktual + 1
    lista_studentów.append(nowy_student)
    print("Student " + a + " "+ b + " został dodany")
    return aktual

#Program
print("Witamy w Usosie co chciałbyś zrobić")
dzialanie = 0
while dzialanie != 7: 
    dzialanie = int(input("""1 - wyświetl oceny wszystkich Studentów
    2 - dodaj ocene 
    3 - usun ocene
    4 - wyswietl oceny Studenta  dla podanego ID
    5 - dodaj przedmiot
    6 - dodaj studenta
    7 - zakończ program
    """))
    if dzialanie == 1: 
        show_usos(students_list,USOS,grades_list)
    elif dzialanie == 2:
        dodawanie_oceny(students_list,USOS,grades_list,aktual_id)
    elif dzialanie == 3:
        usun_ocene(students_list,USOS,grades_list)
    elif dzialanie == 4:
        show_id(students_list,USOS,grades_list)
    elif dzialanie == 5:
        dodaj_przedmiot(USOS.subjects)
    elif dzialanie == 6:
        aktual_id = dodaj_studenta(students_list, aktual_id)
    elif dzialanie == 7:
        print("Dziękuję za urzytkowanie, miłego dnia")
    else: 
        print("Podałeś niewłaściwą wartość dla działąnie programu")

