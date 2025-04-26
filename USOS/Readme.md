# 🎓 USOS Simulator – System Zarządzania Ocenami Studentów

Rozbudowana symulacja systemu **USOS** (Uniwersytecki System Obsługi Studiów) umożliwiająca zarządzanie studentami, przedmiotami, ocenami, uprawnieniami oraz wyświetlaniem danych. Docelowo projekt składa się z backendu w **Pythonie** oraz frontendowego interfejsu w **React.js**. W aktualnej wersji backend wspiera funkcjonalności CRUD oraz uprawnienia użytkowników.

Projekt powstał w ramach kursu **Programowanie Skryptowe** na AGH.

---

## 📂 Struktura projektu (finalna)

```
USOS_Simulator/
├── backend/
│   ├── main.py                # Główne API (FastAPI lub Flask)
│   ├── models.py              # Modele danych (Student, Subject, Grade)
│   ├── crud.py                # Operacje CRUD na bazie danych
│   ├── database.py            # Połączenie z bazą danych (SQLAlchemy / SQLite)
│   ├── schemas.py             # Schematy danych (pydantic)
│   ├── utils.py               # Funkcje pomocnicze (np. import z pliku, walidacje)
│   └── tests/
│       └── test_crud.py       # Testy jednostkowe backendu
├── frontend/
│   ├── src/
│   │   ├── components/        # Komponenty React (lista studentów, formularze)
│   │   ├── pages/             # Widoki (Dashboard, Przedmioty, Oceny)
│   │   ├── App.js             # Główna aplikacja React
│   │   └── index.js           # Punkt startowy frontendu
│   └── package.json           # Konfiguracja projektu React
├── data/
│   └── sample_data.txt        # Przykładowa baza danych (pliki tekstowe)
└── README.md                  # Instrukcja i opis projektu
```

---

## 🧩 Funkcjonalności backendu (Python)

- Zarządzanie:
  - Studentami (dodawanie, usuwanie, edycja)
  - Przedmiotami (wykłady, ćwiczenia, tryb zajęć, limit miejsc)
  - Ocenami (dodawanie, usuwanie, przeglądanie)
- Obsługa uprawnień:
  - Role: `read`, `write`
  - Weryfikacja przy operacjach CRUD
- Parsowanie plików tekstowych (import/export bazy danych)
- API RESTful dla frontendu (np. GET /students, POST /grades)
- Testy jednostkowe (pytest)

---

## 🎨 Funkcjonalności frontendu (React.js)

- Dynamiczne widoki:
  - Lista studentów
  - Szczegóły ocen konkretnego studenta
  - Lista przedmiotów (forma, tryb, limity)
- Operacje CRUD (zgodne z uprawnieniami)
- Walidacja danych na froncie (React Hook Form lub Formik)
- Obsługa komunikacji z backendem przez API (axios / fetch)

---

## 🚀 Instrukcja uruchomienia

### Backend (Python)
```bash
cd backend/
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload  # FastAPI
```

### Frontend (React.js)
```bash
cd frontend/
npm install
npm start
```
Frontend dostępny na `http://localhost:3000`, backend na `http://localhost:8000`.

---

## 📊 Przykładowe zapytania do API

- Pobranie wszystkich studentów:
  ```http
  GET /students
  ```
- Dodanie oceny dla studenta:
  ```http
  POST /grades
  {
    "student_id": 1,
    "subject": "Matematyka",
    "grade": "4.5"
  }
  ```

---

## 👨‍💻 Autorzy

- **Mieszko Makowski**
- **Patryk Motylski**
- **Karol Mierzwiński**

Projekt na potrzeby kursu **Programowanie Skryptowe**, AGH, 2025.

