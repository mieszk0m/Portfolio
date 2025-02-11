class Usos {
    constructor(subjects, grades, students) {
        this.subjects = subjects;
        this.grades = grades;
        this.students = students;
    }

    wykazOcenStudentaOId(indeks) {
        let show = "";
        let student = this.students.find((student)=>student.id === indeks)

        if(!student) {
            console.error("Brak studenta z danym ID")
            return;
        }

        for (const subject of this.subjects) {
            show += `\n   ${subject.name}, prowadzący:${subject.lecturer}\n`;
            for (const [student, oceny] of Object.entries(subject.students)) {
                if (parseInt(student) === indeks) {
                    let total = 0;
                        for (const ocena of oceny) {
                            show += `\t${ocena} `;
                            total += parseFloat(ocena);
                        }
                        show += `\n\tŚrednia: ${Math.round(total * 10 / oceny.length) / 10} `;

                }
            }
        }
        console.log("Dane dla studenta ",student.imie,student.nazwisko);
        console.log(show);

    }
    wykazDlaPrzedmiotu(subjectName) {
        console.log(this.subjects);
        let subject = this.subjects.find((subject) => subject.name.toUpperCase() === subjectName.toUpperCase());
        if(!subject) {
            console.error("ERR");
            return;
        }
        let output = '';
        for(let studentKey in subject.students){
            console.log(studentKey);
            console.log(this.students);
            let studentObj = this.students.find((student)=> student.id ==studentKey )
            output += `${studentObj.imie} ${studentObj.nazwisko}\t`;
            let studentGrades = subject.students[studentKey];
            for(let grade of studentGrades) {
                output += `${grade}\t`
            }
            output += '\n';
        }
        console.log(output);


    }

    dodajPrzedmiot(subjectName) {
        const lista = this.subjects.map((subject) => subject.name);
        if (!lista.includes(subjectName)) {
            const podaneMax = parseInt(prompt("Podaj maksymalną ilość studentów tego przedmiotu"));
            const przedmiot = new Subject(subjectName, podaneMax);
            this.subjects.push(przedmiot);
        } else {
            console.log("Ten przedmiot znajduje się już w Usosie");
        }
    }

    usunOcene(index, przedmiot, ocena) {
        let usunieto = 0;

        let subject = this.znajdzPrzedmiotPoNazwie(przedmiot);
        if(!subject) {
            console.error("ERR");
            return;
        }
        if(!subject.students[index]) {
            console.error("Err przy wyszukiwaniu ocen");
            return;
        }
        let gradesOld = subject.students[index];

        let grades = gradesOld.filter((grade)=> grade != ocena);
        subject.students[index] = grades;


        let filtered = this.grades.filter((grade)=> {
            if(grade.student !== index) return true;
            if(grade.subject.name.toUpperCase() !== przedmiot.toUpperCase()) return true;
            if(grade.grade !== ocena) return true;
            return false;
        })
        this.grades = filtered;
    }
    znajdzPrzedmiotPoNazwie(subjectName) {
        return this.subjects.find((subject)=>subjectName.toUpperCase() === subject.name.toUpperCase())
    }

    dodajOcene(index, przedmiot, ocena, ostatni) {
        let zlyPrzedmiot = 0;
        let dodano = 0;

        let subject = this.znajdzPrzedmiotPoNazwie(przedmiot);
        if(!subject) {
            console.error("Brak takiego przedmiotu");
        }
        const slownik = subject.students;
                for (const [student, wartosc] of Object.entries(slownik)) {
                    console.log(student);
                    if (parseInt(student) === parseInt(index)) {
                        wartosc.push(ocena);
                        const nowaOcena = new Grade(student, subject, ocena);
                        this.grades.push(nowaOcena);
                        dodano = 1;
                    }
                }
        // if (dodano === 0) {
        //     const imie = prompt("Dodajemy nowego studenta podaje jego imię:");
        //     const nazwisko = prompt("nazwisko: ");
        //     for (let subject of this.subjects) {
        //         if (subject.name === przedmiot) {
        //             ostatni++;
        //             const studentDodawany = new Student(ostatni, nazwisko, imie);
        //             const nowaOcena = new Grade(studentDodawany, subject, ocena);
        //             this.grades.push(nowaOcena);
        //             subject.students[studentDodawany] = [ocena];
        //         }
        //     }
        // }
        // if (zlyPrzedmiot === 0) {
        //     console.log("Nie ma takiego przedmiotu");
        // }
        if(dodano == 0 ) {

        }
    }
}
class Student {
    constructor(id, nazwisko, imie) {
        this.id = id;
        this.nazwisko = nazwisko;
        this.imie = imie;
    }
}
class Subject {
    constructor(name, max, lecturer) {
        this.name = name;
        this.max = max;
        this.lecturer = lecturer;
        this.students = {};
    }

    wypisanie() {
        console.log(this.name);
        console.log(`  Maksymalna liczba studentów: ${this.max}`);
        console.log(`  Aktualna liczba studentów: ${Object.keys(this.students).length}`);
        console.log("  Zapisani studenci:");
        for (const student of Object.keys(this.students)) {
            const nazwa = `${student.imie}_${student.nazwisko}`;
            console.log(`    ${nazwa}`);
        }
    }
}

class Grade {
    constructor(student, subject, grade) {
        this.student = student;
        this.subject = subject;

        const allowedGrades = ["2.0", "3.0", "3.5", "4.0", "4.5", "5.0"];
        if (!allowedGrades.includes(grade)) {
            console.error("Podano ocene z poza zakresu");
            return; // Early exit if invalid grade
        }
        this.grade = grade;
    }
}