def wyswietlanie_usos(lista_przedmiotow:list[str],lista_uczniow:list[list[str]],lista_ocen:list[list[list[float]]])->None:
    print("""---------------------------------+----------+------------------------------+ 
Przedmiot          |Studenci                |Oceny                         |
-------------------+------------------------+------------------------------+""")
    wyswietlenie = ""
    x = 0
    for przedmiot in lista_przedmiotow:
        len(przedmiot)
        y = 0
        if przedmiot !=lista_przedmiotow[0]:
            wyswietlenie += """
""" 
        wyswietlenie = wyswietlenie + przedmiot + "     "
        for i   in range (0, (14-len(przedmiot))):
            wyswietlenie = "".join([wyswietlenie," "])
        for student in lista_uczniow[x]:
            if y!=0:
                wyswietlenie += """
                   """
            numer_ucznia = str((y+1))
            wyswietlenie = "".join([wyswietlenie,numer_ucznia,".  ",student,"    "])
            for j in range (0, (16-len(student))):
                wyswietlenie = wyswietlenie + " "
            for ocena in lista_ocen[x][y]:
                ocenka = str(ocena)
                wyswietlenie = " ".join([wyswietlenie,ocenka,ocenka])
            y += 1
        x +=1
    print(wyswietlenie)
    with open (nazwa_pliku,'r') as plik:
        list_of_subject = []
        list_of_students = []
        list_of_grades = []
        for numer_linii, linia in enumerate(plik, start=0):
            czesci =  linia.strip().split(' | ')
            list_of_subject[numer_linii] = czesci[0]
            for i in range (1,len(czesci)):
                uczen  =  czesci[i].strip().split(' : ')
                list_of_students[numer_linii][i-1] = uczen[1]
                oceny = uczen[1].strip().split(' , ')
                for numer_oceny, ocena in enumerate (oceny,start=0):
                    ocena = float(ocena)
                    list_of_grades[numer_linii][i-1][numer_oceny] = ocena
        return list_of_subject, list_of_students, list_of_grades
def pobieranie_bazy_usosa(nazwa_pliku: str) -> (list, list, list):
    with open(nazwa_pliku, 'r') as plik:
        list_of_subject = []
        list_of_students = []
        list_of_grades = []

        for linia in plik:
            czesci = linia.strip().split(' | ')
            list_of_subject.append(czesci[0])
            uczniowie = []
            oceny_po_przedmiotach = []

            for uczen_i_oceny in czesci[1:]:
                uczen, oceny = uczen_i_oceny.split(' : ')
                uczniowie.append(uczen)
                oceny = [float(ocena) for ocena in oceny.split(',')]
                oceny_po_przedmiotach.append(oceny)
            list_of_students.append(uczniowie)
            list_of_grades.append(oceny_po_przedmiotach)

        return list_of_subject, list_of_students, list_of_grades

    